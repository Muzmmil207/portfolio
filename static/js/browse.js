let mobility = document.getElementsByClassName('mobility-btn')
let description = document.querySelector('.description')
let article = document.querySelector('.article')
let image = document.querySelector('.item-image')
let visible = 0

const handleGetData = () => {

    fetch(`/json-format/${visible}/`)
        .then((response) => response.json())
        .then(function (data) {
            article.innerHTML = data.data.name
            image.src = `${data.data.image}`
            description.innerHTML = data.data.article

            if (data.toggle.max) {
                mobility[0].classList.add('not-visible')
            } else {
                mobility[0].classList.remove('not-visible')
            }

            if (data.toggle.min) {
                mobility[1].classList.add('not-visible')
            } else {
                mobility[1].classList.remove('not-visible')
            }
        })


    console.log(image.src)

}


handleGetData()


for (let i = 0; i < mobility.length; i++) {
    mobility[i].addEventListener('click', () => {
        console.log(mobility[i].textContent)
        if (mobility[i].textContent == 'next') {
            visible += 1
        } else if (mobility[i].textContent == 'previous') {
            visible -= 1
        }
        handleGetData()
    })
}