class FichaPaciente
{
    constructor(nome){
        this._nome = nome;
        this._idade = '';
        this._observacao = '';
        this._valor = '';
        this._horarios = [];
    }

    get nome(){
        return this._nome;
    }

    editIdade(idade){
        this._idade = idade;
    }

    editObservacao(observacao){
        this._observacao = observacao;
    }

    editHora(hora){
        this._horarios.push(hora);
    }

    editValor(valor){
        this._valor = valor;
    }
}