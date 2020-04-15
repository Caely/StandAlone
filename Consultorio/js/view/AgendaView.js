class AgendaView
{
    constructor(element){
        this._element = element;
    }

    template(week) {
        return `
        <table>

        <tr>
            
            <tr class="horas">
                <th>Dia/Hora</th>    
                <th>7:00</th>
                <th>8:00</th>
                <th>9:00</th>
                <th>10:00</th>
                <th>11:00</th>
                <th>12:00</th>
                <th>13:00</th>
                <th>14:00</th>
                <th>15:00</th>
                <th>16:00</th>
                <th>17:00</th>
            </tr>

        <tr>
            <th class="dias">Segunda</th>
            ${week.segunda.map(element => `<td class="horas whiteline">${element.paciente ? element.paciente : ''} / ${element.local ? element.local : ''}</td>`).join('')}
        </tr>

        <tr>
            <th class="dias">Terça</th>
            ${week.terca.map(element => `<td class="horas greyline">${element.paciente ? element.paciente : ''} / ${element.local ? element.local : ''}</td>`).join('')}
        </tr>

        <tr>
            <th class="dias">Quarta</th>
            ${week.quarta.map(element => `<td class="horas whiteline">${element.paciente ? element.paciente : ''} / ${element.local ? element.local : ''}</td>`).join('')}
        </tr>

        <tr>
            <th class="dias">Quinta</th>
          ${week.quinta.map(element => `<td class="horas greyline">${element.paciente ? element.paciente : ''} / ${element.local ? element.local : ''}</td>`).join('')}
        </tr>

        <tr>
            <th class="dias">Sexta</th>
          ${week.sexta.map(element => `<td class="horas whiteline">${element.paciente ? element.paciente : ''} / ${element.local ? element.local : ''}</td>`).join('')}
        </tr>

        </table>`;
    }

    update(model){
        this._element.innerHTML = this.template(model);
    }
}

/*
        <tr>
            ${week.semana.map(element =>

                `<tr>
                    ${element.map(dia =>
                    `          
                    <td>${dia.paciente}/${dia.local}</td>`
                    ).join('')}
                </tr>`
            ).join('')}
        </tr>
*/