const socialIconButtons = document.getElementsByClassName("social-icon");

function postToSocialMedia(classList) {
    const content = `Check out these cool AI tools 😎 \n${window.location.href.toString()}`;
    
    if (classList.contains("twitter")) {
        const url = `https://twitter.com/intent/tweet?text=${encodeURIComponent(content)}`;
        window.open(url, '_blank');
    } else if (classList.contains("linkedin")) {
        const url = `https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(window.location.href)}&title=${encodeURIComponent('Check out these cool AI tools 😎')}&summary=${encodeURIComponent(content)}`;
        window.open(url, '_blank');
    } else if (classList.contains("whatsapp")) {
        const url = `https://api.whatsapp.com/send?text=${encodeURIComponent(content)}`;
        window.open(url, '_blank');
    }
}

for (let i = 0; i < socialIconButtons.length; i++) {
    socialIconButtons[i].addEventListener("click", () => {
        postToSocialMedia(socialIconButtons[i].classList);
    });
}


const skillIcons = document.getElementsByClassName("skill-icon");

function updateDescription(id) {
    const descriptionDiv = document.getElementById("description");
    let description = "";

    switch (id) {
        case "googleColab":
            description = "Google Colab: A user-friendly platform for code writing and execution.";
            break;
        case "gradio":
            description = "Gradio: Easily create and share interactive AI apps without extensive coding.";
            break;
        case "openAi":
            description = "OpenAI: Power your projects with advanced language models.";
            break;
        case "playHt":
            description = "PlayHT: Clone voices using AI with high accuracy.";
            break;
        case "huggingFace":
            description = "HuggingFace: The ultimate hub for building and deploying ML models.";
            break;
        case "langChain":
            description = "LangChain: Seamlessly integrate LLMs with external data for powerful applications.";
            break;
        default:
            description = "Select a tool to see its description.";
    }

    descriptionDiv.innerHTML = `<p>${description}</p>`;
}

for (let i = 0; i < skillIcons.length; i++) {
    skillIcons[i].addEventListener("click", (e) => {
        updateDescription(e.target.id);
    });
}
