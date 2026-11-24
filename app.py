import os
import sys

from prueba_carga import prueba_carga


def main():
    if sys.argv[1:] == ["prueba"]:
        prueba_carga()
        return

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto.settings")
    import django
    from django.core.management import call_command

    django.setup()
    from catalogo.datos_ejemplo import cargar_datos_ejemplo

    call_command("migrate", fake_initial=True, verbosity=0)
    cargar_datos_ejemplo()
    call_command("runserver", "8000", use_reloader=False)


if __name__ == "__main__":
    main()
