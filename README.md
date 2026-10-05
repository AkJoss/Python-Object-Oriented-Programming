# Programación Orientada a Objetos con Python 🐍

Este repositorio contiene una colección de prácticas y ejercicios desarrollados para dominar los fundamentos de **Python** y los pilares de la **Programación Orientada a Objetos (POO)**.

## 🚀 Contenido del Repositorio

El proyecto incluye diversos scripts que cubren los siguientes temas:

* **Fundamentos de Lógica:** Control de flujo y ciclos (`while_loop_demo.py`, `conditionals_demo.py`).
* **Programación Orientada a Objetos:** Definición de clases, atributos y métodos (`hogwarts_characters.py`, `hogwarts_oop_demo.py`).
* **Desarrollo de Lógica de Juegos:** Implementaciones sencillas de juegos clásicos (`guessing_game.py`, `car_race_game.py`).
* **Proyectos Temáticos:** Modelado de sistemas usando ejemplos de la cultura popular (`pokemon_battle.py`).
* **Modularización:** Uso de scripts como módulos independientes (`math_functions_demo.py`).

## 🛠 Entorno de Desarrollo

Para la creación y prueba de estos scripts se utilizó el entorno científico de Python:

* **Distribución:** [Anaconda](https://www.anaconda.com/) (Gestión de entornos y paquetes).
* **IDE:** [Spyder](https://www.spyder-ide.org/) (Scientific Python Development Environment).
* **Lenguaje:** Python 3.x.

## 📂 Cómo ejecutar las prácticas

1.  Asegúrate de tener instalado **Anaconda** o **Python** en tu equipo.
2.  Clona este repositorio:
    ```bash
    git clone [https://github.com/AkJoss/Python-Object-Oriented-Programming.git](https://github.com/AkJoss/Python-Object-Oriented-Programming.git)
    ```
3.  Puedes abrir los archivos directamente en **Spyder** para ejecutarlos por secciones o usar la terminal:
    ```bash
    python NombreDelArchivo.py
    ```

## Car race (`car_race_game.py`)

This script needs **pygame** and a Python version that has pygame wheels
(tested with **Python 3.13** / Anaconda). **Python 3.14** may fail to install
pygame until wheels are published.

```bash
# Option A — Anaconda (if pygame is already installed there)
python car_race_game.py

# Option B — virtual environment (recommended for Homebrew Python)
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python car_race_game.py
```

A window opens; the first car past the finish line wins and the name is printed in the terminal.

