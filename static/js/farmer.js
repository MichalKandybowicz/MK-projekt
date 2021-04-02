const dice2 = [
    ["rabbit", "/static/farm_img/rabbit.png", ],
    ["rabbit", "/static/farm_img/rabbit.png"],
    ["rabbit", "/static/farm_img/rabbit.png"],
    ["bear", "/static/farm_img/bear.png"],
    ["bear", "/static/farm_img/bear.png"],
    ["elephants", "/static/farm_img/elephants.png"],
    ["giraffe","/static/farm_img/giraffe.png"],
    ["rabbit", "/static/farm_img/rabbit.png", ],
    ["rabbit", "/static/farm_img/rabbit.png"],
    ["rabbit", "/static/farm_img/rabbit.png"],
    ["bear", "/static/farm_img/bear.png"],
    ["bear", "/static/farm_img/bear.png"],
    ["elephants", "/static/farm_img/elephants.png"],
    ["giraffe","/static/farm_img/giraffe.png"],
    ["wolf","/static/farm_img/wolf.png"],
];

const dice1 = [
    ["rabbit", "/static/farm_img/rabbit.png"],
    ["rabbit", "/static/farm_img/rabbit.png"],
    ["rabbit", "/static/farm_img/rabbit.png"],
    ["rabbit", "/static/farm_img/rabbit.png"],
    ["rabbit", "/static/farm_img/rabbit.png"],
    ["bear", "/static/farm_img/bear.png"],
    ["bear", "/static/farm_img/bear.png"],
    ["bear", "/static/farm_img/bear.png"],
    ["elephants", "/static/farm_img/elephants.png"],
    ["giraffe","/static/farm_img/giraffe.png"],
    ["wolf","/static/farm_img/wolf.png"],
    ["elephants", "/static/farm_img/elephants.png"],
];

const troop = {
    "rabbit": 50,
    "bear": 20,
    "elephants": 30,
    "giraffe": 8,
}

const diceButton = document.getElementById('roll-dice');
diceButton.onclick = dice;

const exchangeButton_rabbit = document.getElementById('rabbit-to-bear');
exchangeButton_rabbit.onclick = rabbitToBear;

function rabbitToBear(){
    // const elToDelete = document.getElementsByClassName(".rabbit")
    // elToDelete.splice(0, 6)
    addingAnimal("bear")

}

function dice() {
    const rNum1 = Math.floor(Math.random() * dice1.length);
    const rNum2 = Math.floor(Math.random() * dice2.length);
    document.getElementById("dice1").src = dice1[rNum1][1];
    document.getElementById("dice2").src = dice2[rNum2][1];

    if(dice1[rNum1][0] ==="wolf" || "wolf" === dice2[rNum2][0]){ // if wolf
        for(const key in troop) {
            const animalToDelete = document.querySelectorAll("."+key);
            troop[key] =troop[key] + animalToDelete.length;
        }

        const elToDelete = document.querySelectorAll(".animal");
        for (const el of elToDelete) {
            el.remove();
        }
    }

    else if (dice1[rNum1][0] === dice2[rNum2][0]) { // two same
            addingAnimals(dice1[rNum1][0], 2)
        }
    else if (dice1[rNum1][0] !== dice2[rNum2][0]){
        // kostka 1
        addingAnimals(dice1[rNum1][0], 1)
        // kostka 2
        addingAnimals(dice2[rNum2][0], 1)
    }
}


function addingAnimals(animal, x){
    const howMany = document.querySelectorAll("."+animal).length
    const howManyAdd = Math.floor((howMany + x )/2)
    troop[animal] = troop[animal] - howManyAdd


    if (troop[animal] >= 0){ //
        for (let i = 0; i < howManyAdd; i++) {
            addingAnimal(animal)
        }
    }
    if (troop[animal] < 0){
        for (let i = 0; i < ((howManyAdd - troop[animal])*-1); i++) {
        addingAnimal(animal)
        }
    }
    if(troop[animal] < 0){
        troop[animal] = 0
    }

}

function addingAnimal(animal){
    const el = document.createElement("img");
    el.src = "/static/farm_img/"+animal+".png";
    el.className = animal;
    el.classList.add("animal");
    troop[animal] =- 1

    const div = document.getElementById(animal);
    div.appendChild(el);
}

