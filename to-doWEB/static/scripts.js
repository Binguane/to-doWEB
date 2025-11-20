function showInputField(){
    const inputField = document.getElementById("inputField")
    inputField.classList.remove("hidden")
}

function hideInputField(){
    const inputField = document.getElementById("inputField")
    inputField.classList.add("hidden")
}

function pushTask() {
    const input = document.getElementById("userInput")
    const inputValue = input.value.trim()
    const todoLi = document.getElementById("todoLi")
    todoLi.classList.add("to-do-li")

    if (inputValue) {
        const item = document.createElement("div")
        const header = document.createElement("h2")
        const par = document.createElement("p")
        const editBtn = document.createElement("button")
        editBtn.textContent = "Edit"
        const deleteBtn = document.createElement("button")
        deleteBtn.textContent = "Delete"

        item.classList.add("item")
        par.textContent = inputValue
        editBtn.classList.add("edit-btn")
        deleteBtn.classList.add("delete-btn")
        item.append(par, editBtn, deleteBtn)
        todoLi.append(item)
        hideInputField()
        
        deleteBtn.addEventListener("click", e => {
            item.remove()
        })
        
        editBtn.addEventListener("click", () => {
            const newTask = prompt("Insert your text")
            if (newTask.trim()) {
                par.textContent = newTask
                item.append(par)
            }
        })
        
    }
    input.value = ""
    
    
}

function showSignUp() {
    document.getElementById("logIn").classList.add("hidden")
    document.getElementById("signUp").classList.remove("hidden")
}

function showLogIn() {
    document.getElementById("logIn").classList.remove("hidden")
    document.getElementById("signUp").classList.add("hidden")
}

profileBtn = document.getElementById("profileBtn")
profileBtn.addEventListener("click", () => {
    window.location.href = "https://user_profile";

    fetch("/home" {
        method:"POST",
        headers:{
            'Content-Type': 'application/json'
        }
        body:JSON.stringify()
})