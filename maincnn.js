const api_route = 'http://127.0.0.1:8000/predict_cnn';

function predict() {
    const input = document.getElementById('input_sentence');
    const sampleCard = document.querySelector('.sample_card');
    const sentence = input.value;
    
    // Reset text and show loading
    input.value = sentence;
    sampleCard.innerHTML = '';

    // Check if the input is empty
    if (sentence.trim() === '') {
        // Show notify message
        const notifyMessage = document.getElementById('notifyMessage');
        notifyMessage.style.display = 'block';
        // Hide notify message after 3 seconds
        setTimeout(() => {
            notifyMessage.style.display = 'none';
        }, 2000);
        return; // Exit the function early
    }

    // Predict
    axios.get(api_route, {
        params: {
            text: sentence
        }
    }).then((response) => {
        const sentiment = response.data.sentiment;
        let imageSrc;

        if (sentiment === 'ข้อความนี้มีลักษณะไปในทางเชิงลบ') {
            imageSrc = "Image/web_redbar.png";
        } else if (sentiment === 'ข้อความนี้มีลักษณะไปในทางเชิงบวก') {
            imageSrc = "Image/web_greenbar.png";
        }

        sampleCard.innerHTML = `
            <img src="${imageSrc}" alt="sentiment image" />
            <p>${sentiment}</p>
        `;
    }).catch((error) => {
        console.log(error);
    });
}
