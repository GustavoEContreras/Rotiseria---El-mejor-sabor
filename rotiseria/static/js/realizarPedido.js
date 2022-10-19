
/*
 Verificar que la fecha del pedido sea la fecha actual, no permitir que sea una fecha
anterior.
*/
const inputFechaEntrega = document.getElementById('fechaDelPedido');

const fechaActual = new Date();
const anioActual = fechaActual.getFullYear();
let mesActual = fechaActual.getMonth() + 1;
if (mesActual < 10)
{
    mesActual = "0" + mesActual.toString();
}
else{
    mesActual = mesActual.toString();
}
let diaActual  = new Date().getDate();
if (diaActual < 10)
{
    diaActual = "0" + diaActual.toString();
}
else
{
    diaActual = diaActual.toString();
}
inputFechaEntrega.value = anioActual.toString() + "-" + mesActual + "-" + diaActual;
inputFechaEntrega.setAttribute('min', anioActual.toString() + "-" + mesActual + "-" + diaActual); //  Se indica la fecha minima del pedido (la fecha actual)

// 10:00AM -- 14:00PM                   Horarios donde no se puede iniciar un pedido:   13:31PM -- 20:29 PM
// 20:30 PM -- 01:00AM                                                                  00:31AM -- 09:59AM
const botonRealizarPedido = document.getElementById('submitButton');
const inputHoraDesde = document.getElementById('horaDesde');
const inputMinutoDesde = document.getElementById('minutoDesde');

function verificarHorario(event)    // El horario del pedido debe ser correcto, caso contrario, un cartel es indicado y se cancela el intento de realizar el pedido
{
    let horaDesde = parseInt(inputHoraDesde.value,10);
    let minutoDesde = parseInt(inputMinutoDesde.value,10);

    if (
        ((horaDesde > 13) ||  ((horaDesde === 13) && (minutoDesde > 30))) && 
        ((horaDesde < 20) || ((horaDesde === 20) && (minutoDesde <= 30))) 
        )
    {
        alert('El pedido no puede ser entregado fuera del horario de la rotiseria');
        event.preventDefault();
    }
    else if (
        ((horaDesde >= 1) || (((horaDesde === 0) && (minutoDesde > 30)))) &&
        ((horaDesde < 10))
        )
    {
        alert('El pedido no puede ser entregado fuera del horario de la rotiseria');
        event.preventDefault();
    }


}

botonRealizarPedido.addEventListener('click', verificarHorario);


function verificarMinutos() // Los minutos del horario de pedido deben ser entre 0 y 60
{
    let minutoDesde = parseInt(inputMinutoDesde.value,10);
    if (minutoDesde < 0)
    {
        inputMinutoDesde.value = 55;
    }
    else if (minutoDesde > 55)
    {   
        inputMinutoDesde.value = 0;
    }
}

inputMinutoDesde.addEventListener('change', verificarMinutos);
inputMinutoDesde.addEventListener('onkeyup', verificarMinutos);
inputMinutoDesde.addEventListener('onkeydown', verificarMinutos);


const inputHorarioHasta = document.getElementById("horariosHasta");

function actualizarHorarioHasta()   // El horario "hasta" debe ser hasta 30 minutos despues del horario "desde"
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

inputHoraDesde.addEventListener('change', actualizarHorarioHasta);
inputMinutoDesde.addEventListener('change', actualizarHorarioHasta);

/*
 Una vez finalizada la orden de pedido, se debe realizar el cálculo del total en forma automática, y ese campo debe estar deshabilitado.
*/

class Producto { //Clase Producto
    constructor(nombre, precio, cantidad)
    {
        this.nombre = nombre;
        this.precio = precio;
        this.cantidad = cantidad;
    }
}

let producto1 = new Producto("Tarta de anquin y queso", 700, 1);
let producto2 = new Producto("Bifes de pollo", 400, 2);

let listaProductos = [];
listaProductos.push(producto1);
listaProductos.push(producto2);

const divListaProductos = document.getElementById("listaProductos");
for (let producto of listaProductos) {
    const divPlato = document.createElement("div");
    divPlato.setAttribute("class", "plato");
    divPlato.innerHTML = `
        <div class="row">
            <div class="col-2"></div>
            <div class="col-4">
                <div class="text-center">
                    <p><b>${producto.nombre}</b></p>
                </div>
            </div>
            <div class="col-1">
                <input type="number" value="${producto.precio * producto.cantidad}" readonly class="precioProducto">
            </div>
        </div>
    `
    divListaProductos.appendChild(divPlato);
}






const productos = document.body.getElementsByClassName('precioProducto');
let precioProductos = 0;
for (const producto of productos) {
    precioProductos += parseInt(producto.getAttribute('value'), 10);
}
const inputPrecioProductos = document.getElementById('precioProductos');
inputPrecioProductos.setAttribute('value', precioProductos);

const inputTipoEntregaRetiro = document.getElementById("retiro");
const inputTipoEntregaDelivery = document.getElementById("delivery");
const inputEnvio = document.getElementById('envio');

function actualizarPrecioEnvio()
{
    if (inputTipoEntregaRetiro.checked)
{
    inputEnvio.setAttribute("value", 0);
}
else if (inputTipoEntregaDelivery.checked)
{
    inputEnvio.setAttribute("value",50);
}
}

inputTipoEntregaRetiro.addEventListener("change", actualizarPrecioEnvio);
inputTipoEntregaDelivery.addEventListener("change", actualizarPrecioEnvio);



function actualizarPrecioTotal()
{
    const precioEnvio = parseInt(inputEnvio.getAttribute('value'),10);

    const precioTotal = precioProductos + precioEnvio;

    const inputPrecioTotal = document.getElementById('precioTotal');
    inputPrecioTotal.setAttribute('value', precioTotal);
}

inputTipoEntregaRetiro.addEventListener("change", actualizarPrecioTotal);
inputTipoEntregaDelivery.addEventListener("change", actualizarPrecioTotal);

actualizarPrecioEnvio();
actualizarPrecioTotal();
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
