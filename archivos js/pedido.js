
/*
 Verificar que la fecha del pedido sea la fecha actual, no permitir que sea una fecha
anterior.


*/

/*
 Verificar que el horario para la entrega del pedido, sea un horario en el que el local se
encuentra trabajando.


const inputHoraDesde = document.getElementById('horaDesde');
const inputMinutoDesde = document.getElementById('minutoDesde');


function verificarHorario()
{
    let horaDesde = parseInt(inputHoraDesde.value,10);
    let minutoDesde = parseInt(inputMinutoDesde.value,10);
    switch(horaDesde)
    {
        case 9:
            alert('El pedido no puede ser entregado fuera del horario de la rotiseria');
            inputHoraDesde.value = 10;
            break;
        case 22:
            alert('El pedido no puede ser entregado fuera del horario de la rotiseria');
            inputHoraDesde.value = 21;
            break;
        default:
            break;
    }
    
    switch(minutoDesde)
    {
        case -5:
            inputMinutoDesde.value = 0;
            break;
        case 60:
            inputMinutoDesde.value = 55;
            break;
        default:
            break;
    }

    if (horaDesde === 21 && minutoDesde > 30)
    {
        alert('El pedido no puede ser entregado fuera del horario de la rotiseria');
        inputMinutoDesde.value = 30;
    }
    
}

const inputHorarioHasta = document.getElementById("horariosHasta");

function actualizarHorarioHasta()
{
    let horaHasta = parseInt(inputHoraDesde.value,10);
    let minutoHasta = parseInt(inputMinutoDesde.value,10) + 30;
    if (minutoHasta >= 60)
    {
        minutoHasta -= 60;
        if (minutoHasta === 0)
        {
            minutoHasta = "00";
        }
        else if (minutoHasta === 5)
        {
            minutoHasta = "05";
        }
        else
        {
            minutoHasta = minutoHasta.toString();
        }
        horaHasta += 1;
        horaHasta = horaHasta.toString();
        inputHorarioHasta.value = String.prototype.concat(horaHasta,":",minutoHasta);
    }
    else{
        inputHorarioHasta.value = String.prototype.concat(horaHasta.toString(),":",minutoHasta.toString());
    }
}
inputHoraDesde.addEventListener('change', verificarHorario);
inputHoraDesde.addEventListener('onkeyup', verificarHorario);
inputHoraDesde.addEventListener('onkeydown', verificarHorario);

inputMinutoDesde.addEventListener('change', verificarHorario);
inputMinutoDesde.addEventListener('onkeyup', verificarHorario);
inputMinutoDesde.addEventListener('onkeydown', verificarHorario);
// inputMinutoDesde.addEventListener('change', verificarHorario);

inputHoraDesde.addEventListener('change', actualizarHorarioHasta);
inputMinutoDesde.addEventListener('change', actualizarHorarioHasta);

*/
/*
 Una vez finalizada la orden de pedido, se debe realizar el cálculo del total en forma automática, y ese campo debe estar deshabilitado.

const productos = document.body.getElementsByClassName('precioProducto');
let precioProductos = 0;
for (const producto of productos) {
    precioProductos += parseInt(producto.getAttribute('value'), 10);
}
const inputPrecioProductos = document.getElementById('precioProductos');
inputPrecioProductos.setAttribute('value', precioProductos);

const inputEnvio = document.getElementById('envio');
const precioEnvio = parseInt(inputEnvio.getAttribute('value'),10);

const precioTotal = precioProductos + precioEnvio;

const inputPrecioTotal = document.getElementById('precioTotal');
inputPrecioTotal.setAttribute('value', precioTotal);

*/
/*
 En el caso de que se cambie el estado del pedido a “devuelto” o “cancelado”, requerir al
usuario que ingrese un comentario.
En la página web donde se muestra el listado de pedidos pendientes:
*/

/*
 Ordenarlos por hora y marcar en rojo los que estén atrasados, en naranja los pedidos
para los cuales falta menos de 1 hora para la entrega y en verde los pedidos donde falta
más de 1 hora para la entrega.
*/
