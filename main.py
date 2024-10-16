from classVenta import Venta

venta = Venta()

venta.set_id_venta(1)
venta.set_fecha("15/10/2024")
venta.set_cliente("Victor")
venta.set_productos({
    "Producto A": {"cantidad": 2, "precio_unitario": 10.0},
    "Producto B": {"cantidad": 1, "precio_unitario": 15.0},
    "Producto C": {"cantidad": 3, "precio_unitario": 7.5}
})
venta.set_total()

venta.mostrar_detalle()