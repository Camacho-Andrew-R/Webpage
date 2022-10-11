const characterClasses = ['Smith', 'Butcher', 'Bum'];

class Fighter {
    constructor(Health, Name, characterClass) {
        this.Health = Health;
        this.Name = Name;
        this.characterClass = characterClass
    }
    dealDamage(amount, target) {
        let damage_array = [amount, target];
        return damage_array;
    }
    takeDamage(amount) {
        return amount;
    }
}

const characterSelect = function characterSelect(event) {
    const selection = document.getElementById("selection").value;
    let selectionNum = Number(selection);
    let classSelection = characterClasses[selectionNum];
    const Player = new Fighter(10, 'Player', classSelection);
    document.getElementById("test").innerHTML = Player.Name;
    return Player;
}

document.getElementById("selectionButton").addEventListener("click", characterSelect);