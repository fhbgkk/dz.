SELECT
    patients.id,
    patients.first_name,
    patients.last_name,
    doctors.name AS doctor_name
FROM patients
JOIN patient_doctor ON patients.id = patient_doctor.patient_id
JOIN doctors ON patient_doctor.doctor_id = doctors.id;

SELECT
    doctors.id AS doctor_id,
    doctors.name AS doctor_name,
    patients.id AS patient_id,
    patients.first_name,
    patients.last_name,
    diseases.name AS disease_name
FROM doctors
JOIN patient_doctor ON doctors.id = patient_doctor.doctor_id
JOIN patients ON patient_doctor.patient_id = patients.id
JOIN patient_disease ON patients.id = patient_disease.patient_id
JOIN diseases ON patient_disease.disease_id = diseases.id;

SELECT
    patients.id,
    patients.first_name,
    patients.last_name,
    procedures.name AS procedure_name
FROM patients
JOIN patient_procedure ON patients.id = patient_procedure.patient_id
JOIN procedures ON patient_procedure.procedure_id = procedures.id;
