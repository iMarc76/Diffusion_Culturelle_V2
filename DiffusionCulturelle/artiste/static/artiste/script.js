    var currentStep = 1;
    const totalSteps = 3;


function validateStep(step) {
    let isValid = true;
    console.log("Validation de l'étape: ", step); // Pour le débogage
    console.log("Validation de l'étape: ", currentStep);
    // Exemple : valider tous les champs d'un formulaire de l'étape spécifique
    const fields = document.querySelectorAll("#step" + step + " input, #step" + step + " select, #step" + step + " textarea");

    fields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            // Afficher un message d'erreur ou marquer le champ comme invalide
            field.classList.add("is-invalid"); // Classe Bootstrap pour les erreurs
        } else {
            field.classList.remove("is-invalid");
        }
    });

    return isValid;
}

document.getElementById("nextBtn").addEventListener("click", function() {
    if (currentStep < totalSteps) {
        // Vérifier si l'étape actuelle est valide avant de passer à la suivante
        if (validateStep(currentStep)) {
            currentStep++;
            showStep(currentStep);
        }
        else {

            // Ajoutez éventuellement du code ici pour gérer le cas où la validation échoue
            console.log("Validation échouée pour l'étape " + currentStep);
        }
    }
});


    function showStep(step) {

        // Cacher toutes les étapes
        for (let i = 1; i <= totalSteps; i++) {
            document.getElementById("step"+i).classList.add("d-none");
        }

        // Afficher l'étape demandée
        document.getElementById("step" + step).classList.remove("d-none");

        // Gérer l'affichage des boutons
        if (step === 1) {
            document.getElementById("prevBtn").classList.add("d-none");
        } else {
            document.getElementById("prevBtn").classList.remove("d-none");
        }

        if (step === totalSteps) {
            document.getElementById("nextBtn").classList.add("d-none");
            document.getElementById("submitBtn").classList.remove("d-none");
        } else {
            document.getElementById("nextBtn").classList.remove("d-none");
            document.getElementById("submitBtn").classList.add("d-none");
        }
    }



    document.getElementById("prevBtn").addEventListener("click", function() {
        if (currentStep > 1) {
            currentStep--;
            showStep(currentStep);
        }
    });

    // Initialiser le formulaire
    showStep(currentStep);









