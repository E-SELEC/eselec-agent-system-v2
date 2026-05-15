---
source_url: https://code.claude.com/docs/es/worktrees
fetched_url: https://code.claude.com/docs/es/worktrees.md
category: Crear con Claude Code, agentes y automatizacion
status: 200
scraped_at: 2026-05-15T14:27:41+00:00
sha256_16: 185cbc68280a40ed
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ejecutar sesiones paralelas con worktrees

> Aisle sesiones paralelas de Claude Code en worktrees de git separados para que los cambios no colisionen. Cubre la bandera `--worktree`, aislamiento de subagentes, `.worktreeinclude`, limpieza y hooks de VCS no-git.

Un [git worktree](https://git-scm.com/docs/git-worktree) es un directorio de trabajo separado con sus propios archivos y rama, compartiendo el mismo historial de repositorio y remoto que su checkout principal. Ejecutar cada sesión de Claude Code en su propio worktree significa que las ediciones en una sesión nunca tocan archivos en otra, por lo que puede tener a Claude construyendo una característica en una terminal mientras corrige un error en una segunda.

Esta página cubre el aislamiento de worktree en la CLI. Todo lo siguiente asume un repositorio de git. Para otros sistemas de control de versiones, consulte [Control de versiones no-git](#non-git-version-control). La [aplicación de escritorio](/es/desktop#work-in-parallel-with-sessions) crea un worktree para cada nueva sesión automáticamente.

Los worktrees son una de varias formas de ejecutar Claude en paralelo. Aíslan ediciones de archivos, mientras que [subagentes](/es/sub-agents) y [equipos de agentes](/es/agent-teams) coordinan el trabajo en sí. Consulte [Ejecutar agentes en paralelo](/es/agents) para comparar los enfoques, o salte directamente a [Aislar subagentes con worktrees](#isolate-subagents-with-worktrees) para usar worktrees y subagentes juntos.

## Inicie Claude en un worktree

Pase `--worktree` o `-w` para crear un worktree aislado e iniciar Claude en él. De forma predeterminada, el worktree se crea bajo `.claude/worktrees/<value>/` en la raíz de su repositorio, en una nueva rama llamada `worktree-<value>`:

```bash theme={null}
claude --worktree feature-auth
```

Para poner worktrees en otro lugar, configure un [hook `WorktreeCreate`](#non-git-version-control). Ejecute el comando nuevamente con un nombre diferente en otra terminal para iniciar una segunda sesión aislada:

```bash theme={null}
claude --worktree bugfix-123
```

Si omite el nombre, Claude genera uno como `bright-running-fox`:

```bash theme={null}
claude --worktree
```

También puede pedirle a Claude que "trabaje en un worktree" durante una sesión, y creará uno con la herramienta [`EnterWorktree`](/es/tools-reference).

Antes de usar `--worktree` en un directorio por primera vez, acepte el diálogo de confianza del espacio de trabajo ejecutando `claude` una vez en ese directorio. Si la confianza aún no ha sido aceptada, `--worktree` sale con un error y le solicita que ejecute `claude` en el directorio primero, incluso cuando se combina con `-p`.

<Tip>
  Agregue `.claude/worktrees/` a su `.gitignore` para que el contenido del worktree no aparezca como archivos sin seguimiento en su checkout principal.
</Tip>

### Elija la rama base

Los worktrees se ramifican desde la rama predeterminada de su repositorio, `origin/HEAD`, por lo que comienzan desde un árbol limpio que coincide con el remoto. Si no hay remoto configurado o la búsqueda falla, el worktree vuelve a su `HEAD` local actual. Para siempre ramificarse desde `HEAD` local en su lugar, establezca `worktree.baseRef` en `"head"` en [configuración](/es/settings#worktree-settings). Establecer `baseRef` en `"head"` hace que los nuevos worktrees lleven sus commits no enviados y estado de rama de característica, lo cual es útil cuando se aíslan subagentes que necesitan operar en trabajo en progreso. La configuración acepta solo `"fresh"` o `"head"`, no refs de git arbitrarios:

```json theme={null}
{
  "worktree": {
    "baseRef": "head"
  }
}
```

Para ramificarse desde una solicitud de extracción específica, pase el número de PR prefijado con `#`, o una URL completa de solicitud de extracción de GitHub. Claude Code obtiene `pull/<number>/head` de `origin` y crea el worktree en `.claude/worktrees/pr-<number>`:

```bash theme={null}
claude --worktree "#1234"
```

Para control total sobre cómo se crean los worktrees, configure un [hook `WorktreeCreate`](/es/hooks#worktreecreate), que reemplaza completamente la lógica predeterminada de `git worktree`.

## Copie archivos ignorados por git en worktrees

Un worktree es un checkout fresco, por lo que archivos sin seguimiento como `.env` o `.env.local` de su repositorio principal no están presentes. Para copiarlos automáticamente cuando Claude crea un worktree, agregue un archivo `.worktreeinclude` a la raíz de su proyecto.

El archivo utiliza la sintaxis de `.gitignore`. Solo se copian los archivos que coinciden con un patrón y también están ignorados por git, por lo que los archivos rastreados nunca se duplican.

Este `.worktreeinclude` copia dos archivos env y una configuración de secretos en cada nuevo worktree:

```text .worktreeinclude theme={null}
.env
.env.local
config/secrets.json
```

Esto se aplica a worktrees creados con `--worktree`, [worktrees de subagentes](#isolate-subagents-with-worktrees), y sesiones paralelas en la [aplicación de escritorio](/es/desktop#work-in-parallel-with-sessions).

## Aisle subagentes con worktrees

Los subagentes pueden ejecutarse en sus propios worktrees para que las ediciones paralelas no entren en conflicto. Pida a Claude que "use worktrees para sus agentes", o establézcalo permanentemente en un [subagente personalizado](/es/sub-agents#supported-frontmatter-fields) agregando `isolation: worktree` al frontmatter. Cada subagente obtiene un worktree temporal que se elimina automáticamente cuando el subagente termina sin cambios.

## Limpie worktrees

Cuando sale de una sesión de worktree, la limpieza depende de si realizó cambios:

* **Sin cambios**: el worktree y su rama se eliminan automáticamente
* **Existen cambios o commits**: Claude le solicita que mantenga o elimine el worktree. Mantener preserva el directorio y la rama para que pueda regresar más tarde. Eliminar borra el directorio del worktree y su rama, descartando todos los cambios no confirmados y commits
* **Ejecuciones no interactivas**: los worktrees creados con `--worktree` junto con `-p` no se limpian automáticamente ya que no hay solicitud de salida. Elimínelos con `git worktree remove`

Los worktrees de subagentes huérfanos por un bloqueo o ejecución interrumpida se eliminan al inicio una vez que son más antiguos que su configuración [`cleanupPeriodDays`](/es/settings#available-settings), siempre que no tengan cambios no confirmados, archivos sin seguimiento ni commits no enviados. Los worktrees que crea con `--worktree` nunca se eliminan por este barrido.

## Administre worktrees manualmente

Para control total sobre la ubicación del worktree y la configuración de rama, cree worktrees directamente con Git. Esto es útil cuando necesita verificar una rama existente específica o colocar el worktree fuera del repositorio.

Cree un worktree en una nueva rama:

```bash theme={null}
git worktree add ../project-feature-a -b feature-a
```

Cree un worktree desde una rama existente:

```bash theme={null}
git worktree add ../project-bugfix bugfix-123
```

Inicie Claude en el worktree:

```bash theme={null}
cd ../project-feature-a && claude
```

Liste sus worktrees:

```bash theme={null}
git worktree list
```

Elimine uno cuando haya terminado con él:

```bash theme={null}
git worktree remove ../project-feature-a
```

Consulte la [documentación de git worktree](https://git-scm.com/docs/git-worktree) para la referencia completa de comandos. Recuerde inicializar su entorno de desarrollo en cada nuevo worktree: instale dependencias, configure entornos virtuales, o ejecute lo que requiera la configuración de su proyecto.

## Control de versiones no-git

El aislamiento de worktree usa git de forma predeterminada. Para SVN, Perforce, Mercurial u otros sistemas, configure [hooks `WorktreeCreate` y `WorktreeRemove`](/es/hooks#worktreecreate) para proporcionar lógica de creación y limpieza personalizada. Debido a que el hook reemplaza el comportamiento predeterminado de git, [`.worktreeinclude`](#copy-gitignored-files-into-worktrees) no se procesa cuando usa `--worktree`. Copie cualquier archivo de configuración local dentro de su script de hook en su lugar.

Este hook `WorktreeCreate` lee el nombre del worktree desde stdin, verifica una copia de trabajo fresca de SVN e imprime la ruta del directorio para que Claude Code pueda usarla como el directorio de trabajo de la sesión:

```json theme={null}
{
  "hooks": {
    "WorktreeCreate": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'NAME=$(jq -r .name); DIR=\"$HOME/.claude/worktrees/$NAME\"; svn checkout https://svn.example.com/repo/trunk \"$DIR\" >&2 && echo \"$DIR\"'"
          }
        ]
      }
    ]
  }
}
```

Emparéjelo con un hook `WorktreeRemove` para limpiar cuando la sesión termina. Consulte la [referencia de hooks](/es/hooks#worktreecreate) para el esquema de entrada y un ejemplo de eliminación.

## Véase también

Los worktrees manejan el aislamiento de archivos. Las páginas relacionadas a continuación cubren la delegación de trabajo en esos checkouts aislados y el cambio entre las sesiones que crea:

* [Subagentes](/es/sub-agents): delegue trabajo a agentes aislados dentro de una sesión
* [Equipos de agentes](/es/agent-teams): coordine múltiples sesiones de Claude automáticamente
* [Administrar sesiones](/es/sessions): nombre, reanude y cambie entre conversaciones
* [Sesiones paralelas de escritorio](/es/desktop#work-in-parallel-with-sessions): sesiones respaldadas por worktree en la aplicación de escritorio
