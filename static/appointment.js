function change() {
    const department = document.getElementById("department").value;
    const doctorSelect = document.getElementById("doctor");

    // Clear previous options
    doctorSelect.innerHTML = "";

    if (department === "Ent") {
      // Add new options for ENT department
      const option1 = document.createElement("option");
      option1.value = "rajesh";
      option1.text = "Dr Rajesh";
      doctorSelect.appendChild(option1);

      const option2 = document.createElement("option");
      option2.value = "deepak";
      option2.text = "Dr Deepak";
      doctorSelect.appendChild(option2);
    }
  }