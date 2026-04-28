"use strict";
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("uploadForm");
    const loading = document.getElementById("loading");
    const results = document.getElementById("results");

    // Toggle JD input mode UI
    const jdUploadSection = document.getElementById("jdUploadSection");
    const jdPasteSection = document.getElementById("jdPasteSection");
    document.querySelectorAll('input[name="jdMode"]').forEach((radio) => {
        radio.addEventListener("change", () => {
            if (radio.value === "upload") {
                jdUploadSection.classList.remove("hidden");
                jdPasteSection.classList.add("hidden");
            } else {
                jdUploadSection.classList.add("hidden");
                jdPasteSection.classList.remove("hidden");
            }
        });
    });

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const resumeInput = document.getElementById("resume");
        const jdFileInput = document.getElementById("jd");
        const jdTextInput = document.getElementById("jdText");
        const jdMode = document.querySelector('input[name="jdMode"]:checked').value;

        // Validate required fields
        if (!resumeInput.files.length || (jdMode === "upload" && !jdFileInput.files.length)) {
            alert("Please provide both Resume and Job Description.");
            return;
        }

        const formData = new FormData();
        formData.append("resume", resumeInput.files[0]);
        formData.append("jd_input_type", jdMode);

        if (jdMode === "upload") {
            formData.append("jd_file", jdFileInput.files[0]);
        } else {
            formData.append("jd_text", jdTextInput.value);
        }

        loading?.classList.remove("hidden");
        results?.classList.add("hidden");

        try {
            const response = await fetch("http://localhost:8000/analyze", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();
            loading?.classList.add("hidden");

            if (data.error) {
                alert("Error: " + data.error);
                return;
            }

            // Update UI with actual response fields
            document.getElementById("overallScore").innerText = data.total_score;
            document.getElementById("searchability").innerText = data.searchability.score;
            document.getElementById("hardSkill").innerText = data.hard_skills.score;
            document.getElementById("softSkill").innerText = data.soft_skills.score;

            const tips = document.getElementById("tips");
            tips.innerHTML = "";
            (data.recruiter_tips.suggestions || []).forEach((tip) => {
                const li = document.createElement("li");
                li.innerText = tip;
                tips.appendChild(li);
            });

            results?.classList.remove("hidden");
        } catch (err) {
            loading?.classList.add("hidden");
            alert("Something went wrong. Please try again.");
            console.error(err);
        }
    });
});
