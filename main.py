
# ============================================================
# PROGRAMA PRINCIPAL
# Sistema Integral de Gestión de Clientes, Servicios y Reservas
# Empresa: Software FJ
# ============================================================

from modelos import (
    Cliente,
    ReservaSalas,
    AlquilerEquipos,
    AsesoriaEspecializada,
    Reserva
)

from gestion import SistemaGestion


# ============================================================
# FUNCION PARA EJECUTAR OPERACIONES Y CONTROLAR ERRORES
# ============================================================

def ejecutar_operacion(nombre, operacion):
    print("\n" + "=" * 60)
    print(nombre)
    print("=" * 60)

    try:
        resultado = operacion()

    except Exception as error:
        print(f"ERROR: {error}")

    else:
        print(f"RESULTADO: {resultado}")

    finally:
        print(f"Finalizó la operación: {nombre}")


# ============================================================
# FUNCION PRINCIPAL
# ============================================================

def main():

    print("=" * 60)
    print("   SOFTWARE FJ")
    print("   SISTEMA INTEGRAL DE GESTION")
    print("=" * 60)

    sistema = SistemaGestion()

    # --------------------------------------------------------
    # 1. CREACION DE CLIENTES
    # --------------------------------------------------------

    cliente1 = Cliente(
        "C001",
        "Carlos Rodriguez",
        "carlos@gmail.com",
        "3001234567"
    )

    cliente2 = Cliente(
        "C002",
        "Laura Martinez",
        "laura@gmail.com",
        "3101234567"
    )

    ejecutar_operacion(
        "OPERACION 1: Registrar primer cliente",
        lambda: sistema.registrar_cliente(cliente1)
    )

    ejecutar_operacion(
        "OPERACION 2: Registrar segundo cliente",
        lambda: sistema.registrar_cliente(cliente2)
    )

    # --------------------------------------------------------
    # 2. REGISTRO DE SERVICIOS
    # --------------------------------------------------------

    sala = ReservaSalas(
        "S001",
        "Sala de reuniones",
        50000,
        20,
        "Sede principal"
    )

    equipo = AlquilerEquipos(
        "S002",
        "Alquiler de proyectores",
        15000,
        "Proyector",
        5
    )

    asesoria = AsesoriaEspecializada(
        "S003",
        "Asesoria de software",
        80000,
        "Desarrollo de software",
        "virtual"
    )

    ejecutar_operacion(
        "OPERACION 3: Registrar sala de reuniones",
        lambda: sistema.registrar_servicio(sala)
    )

    ejecutar_operacion(
        "OPERACION 4: Registrar alquiler de equipos",
        lambda: sistema.registrar_servicio(equipo)
    )

    ejecutar_operacion(
        "OPERACION 5: Registrar asesoria especializada",
        lambda: sistema.registrar_servicio(asesoria)
    )

    # --------------------------------------------------------
    # 3. BUSQUEDA DE INFORMACION
    # --------------------------------------------------------

    ejecutar_operacion(
        "OPERACION 6: Buscar cliente C001",
        lambda: sistema.buscar_cliente("C001").describir()
    )

    ejecutar_operacion(
        "OPERACION 7: Buscar servicio S001",
        lambda: sistema.buscar_servicio("S001").describir()
    )

    # --------------------------------------------------------
    # 4. CREACION Y REGISTRO DE RESERVAS
    # --------------------------------------------------------

    reserva1 = Reserva(
        "R001",
        cliente1,
        sala,
        2
    )

    reserva2 = Reserva(
        "R002",
        cliente2,
        equipo,
        3,
        2
    )

    reserva3 = Reserva(
        "R003",
        cliente1,
        asesoria,
        1
    )

    ejecutar_operacion(
        "OPERACION 8: Registrar reserva de sala",
        lambda: sistema.registrar_reserva(reserva1)
    )

    ejecutar_operacion(
        "OPERACION 9: Registrar reserva de equipos",
        lambda: sistema.registrar_reserva(reserva2)
    )

    ejecutar_operacion(
        "OPERACION 10: Registrar reserva de asesoria",
        lambda: sistema.registrar_reserva(reserva3)
    )

    # --------------------------------------------------------
    # 5. CONFIRMAR RESERVAS
    # --------------------------------------------------------

    ejecutar_operacion(
        "OPERACION 11: Confirmar reserva R001",
        lambda: sistema.confirmar_reserva("R001")
    )

    ejecutar_operacion(
        "OPERACION 12: Confirmar reserva R002",
        lambda: sistema.confirmar_reserva("R002")
    )

    ejecutar_operacion(
        "OPERACION 13: Confirmar reserva R003",
        lambda: sistema.confirmar_reserva("R003")
    )

    # --------------------------------------------------------
    # 6. PROCESAR RESERVAS Y CALCULAR COSTOS
    # --------------------------------------------------------

    ejecutar_operacion(
        "OPERACION 14: Procesar reserva de sala",
        lambda: sistema.procesar_reserva(
            "R001",
            descuento=10,
            impuesto=19
        )
    )

    ejecutar_operacion(
        "OPERACION 15: Procesar reserva de equipos",
        lambda: sistema.procesar_reserva(
            "R002",
            descuento=5,
            impuesto=19
        )
    )

    # --------------------------------------------------------
    # 7. PRUEBA DE DEVOLUCION DE EQUIPOS
    # --------------------------------------------------------

    reserva4 = Reserva(
        "R004",
        cliente1,
        equipo,
        1,
        1
    )

    ejecutar_operacion(
        "PRUEBA 5: Registrar reserva adicional de equipos",
        lambda: sistema.registrar_reserva(reserva4)
    )

    ejecutar_operacion(
        "PRUEBA 6: Confirmar reserva R004",
        lambda: sistema.confirmar_reserva("R004")
    )

    ejecutar_operacion(
        "PRUEBA 7: Consultar inventario después de reservar",
        lambda: equipo.cantidad_disponible
    )

    ejecutar_operacion(
        "PRUEBA 8: Cancelar reserva R004",
        lambda: sistema.cancelar_reserva("R004")
    )

    ejecutar_operacion(
        "PRUEBA 9: Consultar inventario después de devolver",
        lambda: equipo.cantidad_disponible
    )

    # --------------------------------------------------------
    # 8. CANCELAR UNA RESERVA
    # --------------------------------------------------------

    ejecutar_operacion(
        "OPERACION 16: Cancelar reserva R003",
        lambda: sistema.cancelar_reserva("R003")
    )

    # --------------------------------------------------------
    # 9. PRUEBAS DE ERRORES
    # --------------------------------------------------------

    ejecutar_operacion(
        "PRUEBA DE ERROR 1: Registrar cliente duplicado",
        lambda: sistema.registrar_cliente(cliente1)
    )

    ejecutar_operacion(
        "PRUEBA DE ERROR 2: Buscar cliente inexistente",
        lambda: sistema.buscar_cliente("C999")
    )

    ejecutar_operacion(
        "PRUEBA DE ERROR 3: Buscar servicio inexistente",
        lambda: sistema.buscar_servicio("S999")
    )

    ejecutar_operacion(
        "PRUEBA DE ERROR 4: Cancelar reserva procesada",
        lambda: sistema.cancelar_reserva("R001")
    )

    # --------------------------------------------------------
    # 10. CONSULTAR INFORMACION GENERAL
    # --------------------------------------------------------

    ejecutar_operacion(
        "LISTADO GENERAL DE CLIENTES",
        lambda: sistema.listar_clientes()
    )

    ejecutar_operacion(
        "LISTADO GENERAL DE SERVICIOS",
        lambda: sistema.listar_servicios()
    )

    ejecutar_operacion(
        "LISTADO GENERAL DE RESERVAS",
        lambda: sistema.listar_reservas()
    )

    ejecutar_operacion(
        "RESUMEN DEL SISTEMA",
        lambda: sistema.obtener_resumen()
    )

    # --------------------------------------------------------
    # 11. FINALIZAR SISTEMA
    # --------------------------------------------------------

    ejecutar_operacion(
        "CIERRE DEL SISTEMA",
        lambda: sistema.cerrar_sistema()
    )


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()
