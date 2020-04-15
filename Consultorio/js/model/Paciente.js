class Paciente
{
    constructor(nome,hora,local){
        this._nome = nome;
        this._hora = hora;
        this._local = local;
    }

    get hora(){
        return this._hora;
    }

    get paciente(){
        return this._nome;
    }

    get local(){
        return this._local;
    }
}