document.addEventListener("DOMContentLoaded", function(){
    
    let display = document.getElementById("display")

    document.querySelectorAll(".calc-btn").forEach(btn => {
        btn.addEventListener("click", function(){
        
            let value = this.innerText

            if(value === "="){
                try{
                    display.value = eval(display.value)
                }catch{
                    display.value = "Error"
                }
            } else {
                display.value += value
            }
        })
    })

    window.clearDisplay = function(){
        display.value = ""
    }
})

document.addEventListener("keydown", function(e){

    let display = document.getElementById("display")

    if("0123456789+-*/.".includes(e.key)){
        display.value += e.key
    }

    if(e.key === "Enter"){
        try{
            display.value = eval(display.value)
        }catch{
            display.value = "Error"
        }
    }

    if(e.key === "Backspace"){
        display.value = display.value.slice(0,-1)
    }
})