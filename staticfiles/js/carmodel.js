const carForm = document.getElementById('car-form')
const carInput = document.getElementById('cars-container')
const carsDataBox = document.getElementById('cars-data-box')


const modelInput = document.getElementById('models-container')
const modelsDataBox = document.getElementById('models-data-box')

const alertbox = document.getElementById('alert-box')
const btnBox = document.getElementById('btn-box')

const modelText = document.getElementById('modal-text')
const carText = document.getElementById('car-text')
const csrf_tok = document.getElementsByName('csrfmiddlewaretoken')

$.ajax({
    type: 'GET',
    url: '/cars-json/',
    success: function(response){
        console.log(response.data)
        const carsData = response.data
        console.log(carsData)
        carsData.map(item=>{
            const option = document.createElement('div')
            option.textContent = item.name
            option.setAttribute('class', 'item')
            option.setAttribute('data-value', item.name)
            option.setAttribute('data-value', item.name)
            carsDataBox.appendChild(option)
        })
    },
    error: function(error){
        console.log(error)
    }
})


//when the content of car-container is changed
carInput.addEventListener('change', e=>{
    console.log(e.target.value)
    const selectedCar = e.target.value

    alertbox.innerHTML=""
    modelsDataBox.innerHTML = ""
    modelText.textContent = "Choose a model"
    modelText.classList.add("default")


    $.ajax({
        type: 'GET',
        url: `models-json/${selectedCar}/`,
        success: function(response){
            console.log(response.data)
            const modelsData = response.data
            modelsData.map(item=>{
                const option = document.createElement('div')
                option.textContent = item.name
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', item.name)
                modelsDataBox.appendChild(option)
            })

            modelInput.addEventListener('change', e=>{
                btnBox.classList.remove('not-visible')
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})

carForm.addEventListener('submit', e=>{
    e.preventDefault()
    console.log('submitted')

    $.ajax({
        type: 'POST',
        url: '/create/',
        data: {
            'csrfmiddlewaretoken': csrf_tok[0].value,
            'car': carText.textContent,
            'model': modelText.textContent,
        },
        success: function(response){
            console.log(response)
            alertbox.innerHTML = `<div class="ui positive message">
                                    <div class="header">
                                    Success
                                    </div>
                                    <p>Your order has been placed</p>
                                </div>`
        },
        error: function(error){
            console.log(error)
            alertbox.innerHTML = `<div class="ui negative message">
                                    <div class="header">
                                    Ops
                                    </div>
                                    <p>Something went wrong</p>
                                </div>`
        }
    })
})