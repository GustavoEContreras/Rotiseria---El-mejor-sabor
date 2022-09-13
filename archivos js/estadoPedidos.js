const listaPedidos = document.getElementById('listaPedidos');

/*
 En el caso de que se cambie el estado del pedido a “devuelto” o “cancelado”, requerir al
usuario que ingrese un comentario.
En la página web donde se muestra el listado de pedidos pendientes:
*/




class Pedido{
    constructor(nombre,fechaPedido,horaPedido,descripcionPedido,tipoEntrega){
          this.nombre=nombre;
          this.fechaPedido=fechaPedido;
          this.horaPedido=horaPedido;
          this.descripcionPedido = descripcionPedido;
          this.tipoEntrega = tipoEntrega;
    }
}
listaPedidos.innerHTML='';
const divPedido1 = document.createElement("div");
let pedido1 = new Pedido("Gustavo Contreras", "12/09/2022","12:00","Marineras de carne c/ papas fritas","Retira por el local");

divPedido1.innerHTML= ` 
    <ul class="list-group list-group-horizontal">
        <a href="#" class="list-group-item list-group-item-action">
            <div class="d-flex w-60 justify-content-between">
            <h5 class="mb-1">${pedido1.nombre}</h5>
            <small class="text-muted">${pedido1.fechaPedido}</small>
            
            </div>
            <div class="d-flex w-60 justify-content-between">
                <p class="mb-1">${pedido1.descripcionPedido}</p>
                <small class="text-muted">Tiempo de entrega estimado</small>
            </div>
            <div class="d-flex w-60 justify-content-between">
                <small class="text-muted">${pedido1.tipoEntrega}</small>
                <small class="text-muted">${pedido1.horaPedido}hs</small>
            </div>
            
        </a>
        <li class="list-group-item">
            <div class="text-center">
                <select class="mt-2 estadoEntrega"seleccionarEstadoPedido">
                    <option value="Pendiente">Pendiente</option>
                    <option value="En preparación">En preparación</option>
                    <option value="En camino">En camino</option>
                    <option value="Entregado">Entregado</option>
                    <option value="Devuelto">Devuelto</option>
                    <option value="Cancelado">Cancelado</option>
                </select>
            </div>
        </li>
    </ul> ` 
listaPedidos.appendChild(divPedido1);

let pedido2 = new Pedido("Paola Romero", "14/09/2022","13:35","Bondiola braseada c/ensalada Caesar","Debe ser entregado por Ozzy Osborne");

let divPedido2 = document.createElement("div");
divPedido2.innerHTML= ` 
    <ul class="list-group list-group-horizontal">
        <a href="#" class="list-group-item list-group-item-action">
            <div class="d-flex w-60 justify-content-between">
            <h5 class="mb-1">${pedido2.nombre}</h5>
            <small class="text-muted">${pedido2.fechaPedido}</small>
            
            </div>
            <div class="d-flex w-60 justify-content-between">
                <p class="mb-1">${pedido2.descripcionPedido}</p>
                <small class="text-muted">Tiempo de entrega estimado</small>
            </div>
            <div class="d-flex w-60 justify-content-between">
                <small class="text-muted">${pedido2.tipoEntrega}</small>
                <small class="text-muted">${pedido2.horaPedido}hs</small>
            </div>
            
        </a>
        <li class="list-group-item">
            <div class="text-center">
                <select class="mt-2 estadoEntrega"seleccionarEstadoPedido">
                    <option value="Pendiente">Pendiente</option>
                    <option value="En preparación">En preparación</option>
                    <option value="En camino">En camino</option>
                    <option value="Entregado">Entregado</option>
                    <option value="Devuelto">Devuelto</option>
                    <option value="Cancelado">Cancelado</option>
                </select>
            </div>
        </li>
    </ul> `  
listaPedidos.appendChild(divPedido2);

let pedido3 = new Pedido("Homero Simpson", "15/09/2022","23:30","Supremas de pollo c/puré mixto","Debe ser entregado por Lenny Leonard");

let divPedido3 = document.createElement("div");
divPedido3.innerHTML= ` 
    <ul class="list-group list-group-horizontal">
        <a href="#" class="list-group-item list-group-item-action">
            <div class="d-flex w-60 justify-content-between">
            <h5 class="mb-1">${pedido3.nombre}</h5>
            <small class="text-muted">${pedido3.fechaPedido}</small>
            
            </div>
            <div class="d-flex w-60 justify-content-between">
                <p class="mb-1">${pedido3.descripcionPedido}</p>
                <small class="text-muted">Tiempo de entrega estimado</small>
            </div>
            <div class="d-flex w-60 justify-content-between">
                <small class="text-muted">${pedido3.tipoEntrega}</small>
                <small class="text-muted">${pedido3.horaPedido}hs</small>
            </div>
            
        </a>
        <li class="list-group-item">
            <div class="text-center">
                <select class="mt-2 estadoEntrega"seleccionarEstadoPedido">
                    <option value="Pendiente">Pendiente</option>
                    <option value="En preparación">En preparación</option>
                    <option value="En camino">En camino</option>
                    <option value="Entregado">Entregado</option>
                    <option value="Devuelto">Devuelto</option>
                    <option value="Cancelado">Cancelado</option>
                </select>
            </div>
        </li>
    </ul> `  
listaPedidos.appendChild(divPedido3);

const selectEstadoEntrega = document.getElementsByClassName('estadoEntrega');


for(let i = 0; i < selectEstadoEntrega.length; i++) {

    selectEstadoEntrega[i].addEventListener('change', function()
    {
        let cajaComentario = document.createElement('input');
        cajaComentario.setAttribute('class', "mt-2");
        cajaComentario.setAttribute('placeholder', 'Comentario');
        cajaComentario.setAttribute('type', 'text');
        // class="mt-2" type="text" placeholder="Comentario"
        if (this.value === "Devuelto" || this.value === "Cancelado") 
        {
            this.parentElement.appendChild(cajaComentario);
        }
        else if (this.parentElement.lastChild.tagName === "INPUT")
        {
            this.parentElement.removeChild(this.parentElement.lastChild);
        }
    });
}






/*
 Ordenarlos por hora y marcar en rojo los que estén atrasados, en naranja los pedidos
para los cuales falta menos de 1 hora para la entrega y en verde los pedidos donde falta
más de 1 hora para la entrega.
*/

/*
let listaAuxiliarPedidos = listaPedidos;

for (let i = 0; i < listaPedidos.length; i++) 
{
    for (let j=0; j < i-1; j++) 
    {
        const divPedido1 = Array.from(listaAuxiliarPedidos.children).indexOf(j);
        const divPedido2 = Array.from(listaAuxiliarPedidos.children).indexOf(j + 1);
        let stringFecha1 = divPedido1.firstChild.firstChild.lastChild.lastChild.innerHTML;
        let stringFecha2 = divPedido2.firstChild.firstChild.lastChild.lastChild.innerHTML;

    }
}
*/