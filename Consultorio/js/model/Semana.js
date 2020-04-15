class Semana
{
    constructor(){
        this._semana = [
            ['','','','','','','','','','',''],
            ['','','','','','','','','','',''],
            ['','','','','','','','','','',''],
            ['','','','','','','','','','',''],
            ['','','','','','','','','','','']];
    }

    get semana() {
        return this._semana;
    }

    get segunda() {
        return this._semana[0];
    }

    get terca() {
        return this._semana[1];
    }

    get quarta() {
        return this._semana[2];
    }

    get quinta() {
        return this._semana[3];
    }

    get sexta() {
        return this._semana[4];
    }

    _getPosition(dia){
        let positions = ['segunda','terca','quarta','quinta','sexta'];

        for(let i = 0;i < positions.length;i++){
            if (dia == positions[i]) return i;
        }

        throw Error ('Dia da semana nao bate');
    }

    adiciona(paciente,dia){
        let posicao = this._getPosition(dia);
        this.semana[posicao][paciente.hora - 7] = paciente;
        //o menos 7 é para definir a posicao do array baseado na hora da consulta
    }
}