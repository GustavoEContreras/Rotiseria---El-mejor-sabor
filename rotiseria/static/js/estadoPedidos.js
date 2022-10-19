const divListaPedidos = document.getElementById('listaPedidos'); // DIV principal donde se añadiran (como hijos) cada div que pertenecera a un pedido
divListaPedidos.innerHTML='';

const fechaActual = new Date(new Date().getFullYear, new Date().getMonth, new Date().getDate());
// Fecha actual sin tener en cuenta la hora del dia actual

class Pedido{ //Clase Pedido, es la clase principal utilizada para almacenar facilmente la informacion de los pedidos. Consta de los siguientes atributos
    constructor(nombre,fechaPedido,horaPedido,descripcionPedido,tipoEntrega,estadoEntrega){
        this.nombre=nombre; // Nombre completo. Tipo String
        this.fechaPedido=fechaPedido; // Fecha del pedido. Objeto Date
        this.fechaPedido.setHours(horaPedido.hora, horaPedido.minutos) // Modificación de fecha pedido para incluir las horas del dia respectivas. Más abajo se define a la clase Hora (utilizada en esta linea de codigo)
        this.descripcionPedido = descripcionPedido; // Descripción del pedido (ingredientes). Tipo String
        this.tipoEntrega = tipoEntrega; // Tipo de entrega del pedido (puede ser retirado en el local o entregado por un cadete asignado). Tipo String
        if ( // Color con el que se representara al pedido. Funciona como una bandera. Se añade como clase en el codigo HTML con el fin de darle su color respectivo al pedido utilizando CSS. Tipo String
            (this.fechaPedido.cantidadDiferenciaEnDias(new Date()) >= 1) || 
            ((this.fechaPedido.esElMismoDia(new Date())) && (!this.fechaPedido.faltaMenosDeUnaHora(new Date()))) //Si la fecha de pedido es una fecha posterior a la actual o es la misma pero con más de una hora de diferencia --> El color del pedido sera verde
            )
            {
                this.colorPedido = "verde";
            }
        else if (
            (this.fechaPedido.cantidadDiferenciaEnDias(new Date()) < 0) ||
            ((this.fechaPedido.esElMismoDia(new Date())) && (this.fechaPedido.faltaMenosDeUnaHora(new Date())) && (this.fechaPedido.esHoraAnterior())) 
            ) // Si la fecha de pedido es una fecha anterior a la actual o es la misma pero con un horario retrasado comparado al actual --> El color del pedido sera rojo
            {
                this.colorPedido = "rojo";
            }
        else if (
            (this.fechaPedido.cantidadDiferenciaEnDias(new Date()) === 0) &&
            ((this.fechaPedido.esElMismoDia(new Date())) && (this.fechaPedido.faltaMenosDeUnaHora(new Date())) && (!this.fechaPedido.esHoraAnterior())) 
        )   // Si la fecha de pedido es la misma que la fecha actual y falta menos de una hora para la entrega del pedido (o para que este sea retirado) --> El color del pedido sera naranja
            {
                this.colorPedido = "naranja";
            }
        if ((estadoEntrega == "Devuelto") || (estadoEntrega == "Cancelado") || (estadoEntrega == "Entregado"))
        {
            this.colorPedido = "";
        }
        this.estadoEntrega = estadoEntrega;
    }
}
class Hora{ //Clase Hora. Utilizada para facilitar la inicializacion de un objeto Date añadiendo la hora del dia correspondinte
    constructor(hora,minutos)
    {
        this.hora = hora; //Horas del dia. Tipo number
        this.minutos = minutos; //Minutos del dia. Tipo number
    }
    horaString(){ // Función que devuelve el horario del dia en el siguiente formato --> "Horas:minutos hs"
        if (this.hora < 10 && this.minutos < 10)
        {
            return ("0" + this.hora.toString() + ":" + "0" + this.minutos.toString() + "hs");
        }
        else if (this.hora < 10 && this.minutos >= 10)
        {
            return ("0" + this.hora.toString() + ":" + this.minutos.toString() + "hs");
        }
        else if (this.hora >= 10 && this.minutos < 10)
        {
            return (this.hora.toString() + ":" + "0" + this.minutos.toString() + "hs");
        }
        else{
            return (this.hora.toString() + ":" + this.minutos.toString() + "hs");
        }
    }
}
// En este apartado, se definen nuevas funciones para los objetos que partan de la clase Date
Date.prototype.cantidadDiferenciaEnDias = function(fechaAComparar) //Devuelve la cantidad de dias de diferencia que hay entre dos fechas.
{
    return Math.round((this - fechaAComparar)/(1000*60*60*24));
}
Date.prototype.agregarDias = function(dias) //Añade dias (o puede restarlos) de la fecha  
    {
        this.setDate(this.getDate() + parseInt(dias));
        return this;
    };
Date.prototype.esElMismoDia = function(fechaAComparar){ //Comprueba que ambas fechas sean el mismo dia (sin importar el horario de ambas)
    if (
        this.getFullYear() === fechaAComparar.getFullYear() &&
        this.getMonth() === fechaAComparar.getMonth() &&
        this.getDate() === fechaAComparar.getDate()
      )
    {
        return true;
    }
    else{
        return false;
    }
}
Date.prototype.faltaMenosDeUnaHora = function(fechaAComparar){ // Indica si ambas fechas son el mismo dia y estas tienen una diferencia de menos de una hora
    const UNA_HORA = 60 * 60 * 1000;
    return ((this - fechaAComparar) < UNA_HORA);
}
Date.prototype.esHoraAnterior = function(fechaAComparar){ //Indica si la fecha a comparar es en un horario y/o fecha posterior
    return ((this - fechaAComparar) <= 0);
}
Date.prototype.compararFechaSuperior = function(fechaAComparar) // Indica si la fecha es mayor a la fecha a comparar (tanto en dia como en el horario)
    {
        if (this > fechaAComparar)
        {
            return true;    // Devuelve la fecha anterior
        }
        else
        {
            return false;
        }
    }
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


const listaPedidos = []; // Lista de pedidos. Tipo array. Utilizada para ordenar los pedidos

const fechaAnterior = new Date(); //Fechas inicializadas para inicializar los correspondientes pedidos. Objeto tipo Date
const fechaPosterior2 = new Date();

// Pedidos inicializados
let pedido1 = new Pedido("Gustavo Contreras", fechaAnterior.agregarDias(-5), new Hora(12,0),"Marineras de carne c/ papas fritas","Retira por el local", "Pendiente");
let pedido2 = new Pedido("Paola Romero", new Date(), new Hora(21,50),"Bondiola braseada c/ensalada Caesar","Debe ser entregado por Ozzy Osborne", "Cancelado");
let pedido3 = new Pedido("Homero Simpson", fechaPosterior2.agregarDias(3), new Hora(22,00),"Supremas de pollo c/puré mixto","Debe ser entregado por Lenny Leonard", "Entregado");

// Pedidos añadidos a la lista de pedidos
listaPedidos[0] = pedido1;
listaPedidos[1] = pedido2;
listaPedidos[2] = pedido3;

// Ordenamiento de los pedidos mediante la función "sort" del array. Esta la definimos para que tenga en cuenta la fecha y hora de cada pedido.
listaPedidos.sort(function(a,b)
    {
        let fecha1 = new Date(a.fechaPedido);
        let fecha2 = new Date(b.fechaPedido);
        return fecha1.getTime() - fecha2.getTime();
    }
)

function getIndiceEstadoEntrega(estadoEntrega)
{
    switch (estadoEntrega)
    {
        case "Pendiente":
            return 0;
        case "En preparación":
            return 1;
        case "En camino":
            return 2;
        case "Entregado":
            return 3;
        case "Devuelto":
            return 4;
        case "Cancelado":
            return 5;
        default:
            return 0;
    }
}

function esElIndiceCorrecto(indice,tipoDeEntrega)
{
    if (tipoDeEntrega === "Pendiente" && indice === 0)
    {
        return 'selected="selected"';
    }
    else if (tipoDeEntrega === "En preparación" && indice === 1)
    {
        return 'selected="selected"';
    }
    else if (tipoDeEntrega === "En camino" && indice === 2)
    {
        return 'selected="selected"';
    }
    else if (tipoDeEntrega === "Entregado" && indice === 3)
    {
        return 'selected="selected"';
    }
    else if (tipoDeEntrega === "Devuelto" && indice === 4)
    {
        return 'selected="selected"';
    }
    else if (tipoDeEntrega === "Cancelado" && indice === 5)
    {
        return 'selected="selected"';
    }
    else{
        return "";
    }
}
// Carga de pedidos en el codigo HTML, todos siguen una estructura igual en cuanto a HTML
for (let auxiliarPedido of listaPedidos)
    {
        const divPedido = document.createElement("div"); // Creación de un DIV donde se agrega un unico pedido
        const horaPedido = new Hora(auxiliarPedido.fechaPedido.getHours(), auxiliarPedido.fechaPedido.getMinutes()); // Creacion de un objeto tipo Hora utilizado de manera auxiliar para facilitar escribir la hora en el siguiente formato --> "Horas:minutos hs" 
        divPedido.innerHTML = `
            <ul class="list-group list-group-horizontal">
                <a href="#" class="list-group-item list-group-item-action ${auxiliarPedido.colorPedido} cardPedido">
                    <span class= "${auxiliarPedido.colorPedido}">
                        <div class="d-flex w-60 justify-content-between">
                        <h5 class="mb-1">${auxiliarPedido.nombre}</h5>
                        <small class="">${auxiliarPedido.fechaPedido.toISOString().substring(0,10)}</small>
                        
                        </div>
                        <div class="d-flex w-60 justify-content-between">
                            <p class="mb-1">${auxiliarPedido.descripcionPedido}</p>
                            <small class="">Tiempo de entrega estimado</small>
                        </div>
                        <div class="d-flex w-60 justify-content-between">
                            <small class="">${auxiliarPedido.tipoEntrega}</small>
                            <small class="">${horaPedido.horaString()}</small>
                        </div>
                    </span>
                </a>
                <li class="list-group-item">
                    <div class="text-center">
                        <select class="mt-2 estadoEntrega"seleccionarEstadoPedido">
                            <option value="Pendiente" ${esElIndiceCorrecto(0,auxiliarPedido.estadoEntrega)}>Pendiente</option>
                            <option value="En preparación" ${esElIndiceCorrecto(1,auxiliarPedido.estadoEntrega)}>En preparación</option>
                            <option value="En camino" ${esElIndiceCorrecto(2,auxiliarPedido.estadoEntrega)}>En camino</option>
                            <option value="Entregado" ${esElIndiceCorrecto(3,auxiliarPedido.estadoEntrega)}>Entregado</option>
                            <option value="Devuelto" ${esElIndiceCorrecto(4,auxiliarPedido.estadoEntrega)}>Devuelto</option>
                            <option value="Cancelado" ${esElIndiceCorrecto(5,auxiliarPedido.estadoEntrega)}>Cancelado</option>
                        </select>
                    </div>
                </li>
            </ul> `
            divListaPedidos.appendChild(divPedido); // El pedido es añadido al DIV principal de la lista de pedidos
    }



const selectEstadoEntrega = document.getElementsByClassName('estadoEntrega'); // Se obtiene una coleccion de todos los elementos SELECT que indican el estado de entrega de un pedido especifico


for(let i = 0; i < selectEstadoEntrega.length; i++) { // A cada uno de estos elementos SELECT se les añade un event listener el cual funciona al momento de ocurrir un evento "change"

    selectEstadoEntrega[i].addEventListener('change', function()
    {
        let cajaComentario = document.createElement('input');
        cajaComentario.setAttribute('class', "mt-2");
        cajaComentario.setAttribute('placeholder', 'Comentario');
        cajaComentario.setAttribute('type', 'text'); // Se añade una caja de comentario si el valor actual del elemento SELECT es "Devuelto" o "Cancelado"
        // class="mt-2" type="text" placeholder="Comentario"
        if ((this.value === "Devuelto" || this.value === "Cancelado") && this.parentElement.lastChild.tagName != "INPUT") 
        {
            this.parentElement.appendChild(cajaComentario);
        }
        else if (this.parentElement.lastChild.tagName === "INPUT" && this.value != "Devuelto" && this.value != "Cancelado") // Si ya existe una caja de INPUT, en caso de que la opcion elegida no sea "Devuelto" o "Cancelado", la caja de comentario correspondiente es eliminada del codigo HTML
        {
            this.parentElement.removeChild(this.parentElement.lastChild);
        }
    });
}








