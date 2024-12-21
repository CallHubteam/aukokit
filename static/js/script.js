async function startVideoCall() {
    try {
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
            alert("Vaizdo skambučių funkcija nepalaikoma šioje naršyklėje. Įsitikinkite, kad naudojate HTTPS protokolą arba atnaujinkite naršyklę.");
            return;
        }
        const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
        const videoElement = document.getElementById('localVideo');
        if (!videoElement) {
            alert("Vaizdo elementas nerastas puslapyje. Patikrinkite HTML struktūrą.");
            return;
        }
        if ('srcObject' in videoElement) {
            videoElement.srcObject = stream;
        } else {
            videoElement.src = window.URL.createObjectURL(stream);
        }
        videoElement.onloadedmetadata = () => {
            videoElement.play();
        };
    } catch (error) {
        console.error(`Klaida: ${error.message}`);
        alert("Klaida: Negalima paleisti vaizdo skambučio. Patikrinkite naršyklės leidimus ir įrenginius.");
    }
}
