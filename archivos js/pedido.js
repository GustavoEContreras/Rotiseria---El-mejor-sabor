/*
 Verificar que la fecha del pedido sea la fecha actual, no permitir que sea una fecha
anterior.
 Verificar que el horario para la entrega del pedido, sea un horario en el que el local se
encuentra trabajando.
 Una vez finalizada la orden de pedido, se debe realizar el cálculo del total en forma automática, y ese campo debe estar deshabilitado.
 En el caso de que se cambie el estado del pedido a “devuelto” o “cancelado”, requerir al
usuario que ingrese un comentario.
En la página web donde se muestra el listado de pedidos pendientes:
 Ordenarlos por hora y marcar en rojo los que estén atrasados, en naranja los pedidos
para los cuales falta menos de 1 hora para la entrega y en verde los pedidos donde falta
más de 1 hora para la entrega.
*/


const dateFechaActual = new Date();

const dateFechaPedido = new Date(document.body.getElementById("fechaDelPedido").value);
alert(dateFechaPedido);

function esFechaActualOPosterior()
{
    let fechaPedido = new Date(dateFechaPedido.value);
    if (fechaPedido >= fechaActual)
    {
        document.getElementById("fechaDelPedido") = fecha;
    }
    else if (fechaPedido < fechaActual)
    {
        document.getElementById("fechaDelPedido") = fechaActual;
    }
}

dateFechaPedido.addEventListener('input', esFechaActualOPosterior());

