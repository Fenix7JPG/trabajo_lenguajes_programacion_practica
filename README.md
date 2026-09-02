# Lenguajes de Programación I — Laboratorio

Repositorio de prácticas de la asignatura **Lenguajes de Programación I**.
---

## Tutorial de Git — desde cero hasta GitHub

### 1. Instalar Git

1. Descarga el instalador oficial: **https://git-scm.com/downloads**
2. Elige tu sistema operativo (Windows, macOS o Linuxy descarga la versión más reciente.
3. En Windows: ejecuta el instalador y deja **todas las opciones por defecto** (instala Git Bash y Git CMD).
4. Verifica la instalación abriendo cmd y ejecutando:

```bash
git --version
```

### 2. Configuración inicial (solo una vez por PC)

Identifica tus commits con tu nombre y correo (usa el mismo correo de tu cuenta de GitHub):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```

### 3. Obtener el proyecto (clone)

```bash
git clone https://github.com/Fenix7JPG/trabajo_lenguajes_programacion_practica.git
cd trabajo_lenguajes_programacion_practica
```

Esto descarga el repositorio completo a tu PC.

### 4. Flujo básico de trabajo

El ciclo diario con Git es siempre el mismo:

```bash
git pull origin main            # Descargar cambios si hubieron
git status                      # Ver qué archivos cambiaron
git add .                       # Preparar TODOS los cambios
git status                      # Ver cambios efectuados por ti
git commit -m "mensaje"         # Guardar los cambios localmente
git push origin main            # Subirlos a GitHub
```


### 5. Ramas (branch)

Una rama permite trabajar en una función sin afectar `main`:

```bash
git branch mi-rama             # Crear la rama
git switch mi-rama             # Cambiarte a ella
# ... trabajas y haces add / commit normalmente ...
git switch main                # Volver a main
git merge mi-rama              # Fusionar tu trabajo en main
git push origin main           # Subir la fusión
```

Atajo para crear y cambiarte en un paso:

```bash
git switch -c mi-rama
```

### 6. Resumen de comandos

| Comando | Para qué sirve |
|---|---|
| `git clone <url>` | Descargar el repositorio |
| `git status` | Ver el estado de los archivos |
| `git add .` | Preparar todos los cambios |
| `git commit -m "msg"` | Guardar cambios con un mensaje |
| `git push origin main` | Subir commits a GitHub |
| `git pull origin main` | Bajar los cambios de GitHub |
| `git branch` | Listar ramas |
| `git branch <nombre>` | Crear una rama |
| `git switch <rama>` | Cambiar de rama |
| `git merge <rama>` | Fusionar una rama en la actual |
| `git log --oneline` | Ver historial de commits |

> **Regla de oro:** antes de empujar, siempre `git pull`; antes de COMMIT, revisa con `git status`.
sisibhjhb