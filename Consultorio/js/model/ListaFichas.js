class ListaFichas
{
    constructor(){
        this._lista = [];
    }

    get lista(){
        return this._lista;
    }

    adiciona(paciente){
        this._lista.push(paciente);
    }

    isInside(nome){
        this._lista.map(function(element){
            if(nome == element.nome) console.log("ta dentro");
        });
    }
}