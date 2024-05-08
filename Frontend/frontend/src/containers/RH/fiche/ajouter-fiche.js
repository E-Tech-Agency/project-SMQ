import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import TimeZoneSelect from 'react-timezone-select';
import '../formation/FormationForm.css';
import { Navigate ,Link} from 'react-router-dom';
import Cookies from 'js-cookie';

function FicheForm() {
    const [name, setName] = useState('');
    const [job_positions, setJobPositions] = useState([]);
    const [job_positionID, setJobPosition] = useState('');
    const [work_mobile, setWorkMobile] = useState('');
    const [work_phone, setWorkPhone] = useState('');
    const [work_email, setWorkEmail] = useState('');
    const [departments, setDepartments] = useState([]);
    const [managers, setManagers] = useState([]);
    const [coachs, setCoachs] = useState([]);
    const [work_addresss, setWorkAddresss] = useState([]);
    const [departmentID, setDepartment] = useState('');
    const [managerID, setManager] = useState('');
    const [coachID, setCoach] = useState('');
    const [work_addressID, setWorkAddress] = useState('');
    const [work_location, setWorkLocation] = useState('');
    const [addresss, setAddresss] = useState([]);
    const [addressID, setAddress] = useState('');
    const [working_hours, setWorkingHours] = useState('');
    const [timezone_field, setTimezoneField] = useState('UTC');
    const [bank_account_number, setBankAccountNumber] = useState('');
    const [home_work_distance, setHomeWorkDistance] = useState('');
    const [martial_status, setMartialStatus] = useState('');
    const [emergency_contact, setEmergencyContact] = useState('');
    const [emergency_phone, setEmergencyPhone] = useState('');
    const [certificate_level, setCertificateLevel] = useState('');
    const [field_of_study, setFieldOfStudy] = useState('');
    const [school, setSchool] = useState('');
    const [cnss, setCnss] = useState('');
    const [cin, setCin] = useState('');
    const [pieces_jointes, setPiecesJointes] = useState(null);
    const [employe_concernes, setEmployes] = useState([]);
    const [employe_concerneID, setEmploye] = useState([]);


    const [ajoutReussi, setAjoutReussi] = useState(false);

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}/RH/dashboard_employe/`)
      .then(response => {
        setEmployes(response.data);
        setManagers(response.data);
        setCoachs(response.data);
      })
      .catch(error => {
        console.error('Erreur lors de la récupération des employés :', error);
      });

    axios.get(`${process.env.REACT_APP_API_URL}/RH/dashboard_job_post/`)
      .then(response => {
        setJobPositions(response.data);
      })
      .catch(error => {
        console.error('Erreur lors de la récupération des position :', error);
    });

    axios.get(`${process.env.REACT_APP_API_URL}/RH/dashboard_address/`)
      .then(response => {
        setAddresss(response.data);
        setWorkAddresss(response.data)
      })
      .catch(error => {
        console.error('Erreur lors de la récupération des address :', error);
      });

    axios.get(`${process.env.REACT_APP_API_URL}/RH/dashboard_department/`)
      .then(response => {
        setDepartments(response.data);
      })
      .catch(error => {
        console.error('Erreur lors de la récupération des departments :', error);
    });
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    const participantData = {
        name: name,
        job_position: job_positionID,
        work_mobile: work_mobile,
        work_phone : work_phone,
        work_email: work_email,
        department: departmentID,
        manager: managerID,
        coach: coachID,
        work_address: work_addressID,
        work_location: work_location,
        address : addressID,
        working_hours: parseFloat(working_hours),
        timezone_field: timezone_field,
        bank_account_number: bank_account_number,
        home_work_distance: home_work_distance,
        martial_status: martial_status,
        emergency_contact: emergency_contact,
        emergency_phone: emergency_phone,
        certificate_level: certificate_level,
        field_of_study: field_of_study,
        school : school,
        cnss: cnss,
        cin: cin,
        pieces_jointes: pieces_jointes,
        employe_concerne: employe_concerneID,
    };

    const headers = {
      'Accept':'*/*',
      "Content-Type":'application/json',
      'X-CSRFToken': Cookies.get('csrftoken')
    };

    axios.post(`${process.env.REACT_APP_API_URL}/RH/create_fiche_employe/`, participantData, { headers: headers })
      .then(response => {
        console.log('Fiche ajouté avec succès :', response.data);
        setName('');
        setJobPosition('');
        setWorkMobile('');
        setWorkPhone('');
        setWorkEmail('');
        setManager('')
        setCoach('')
        setDepartment('');
        setWorkAddress('');
        setWorkLocation('');
        setAddress('');
        setWorkingHours('');
        setTimezoneField('UTC');
        setBankAccountNumber('');
        setHomeWorkDistance('');
        setMartialStatus('');
        setEmergencyContact('');
        setEmergencyPhone('');
        setCertificateLevel('');
        setFieldOfStudy('');
        setSchool('');
        setCnss('');
        setCin('');
        setPiecesJointes(null);
        setEmploye('')

        setAjoutReussi(true);
      })
      .catch(error => {
        console.error('Erreur lors de l\'ajout du fiche :', error);
      });
  };
  if(ajoutReussi){
    return <Navigate to="/Dashboardfiche" />;
}

  return (
    <div className="form-container">
      <div className="form-card">
        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label>
              Nom fiche :
              <input type="text" name="name" value={name} onChange={(e) => setName(e.target.value)} />
            </label>
          </div>
          <div className="form-group">
            <label>
              Work Mobile :
              <input type="text" name="work_mobile" value={work_mobile} onChange={(e) => setWorkMobile(e.target.value)} />
            </label>
          </div>
          <div className="form-group">
            <label>
              Email :
              <input type="email" name="work_email" value={work_email} onChange={(e) => setWorkEmail(e.target.value)} />
            </label>
          </div>
          <div className="form-group">
            <label>
            work phone :
              <input type="text" name="work_phone" value={work_phone} onChange={(e) => setWorkPhone(e.target.value)} />
            </label>
          </div>
          <div className="form-group">
          <label>
            Position :
            <select value={job_positionID} onChange={(e) => setJobPosition(e.target.value)}>
              <option value="">Sélectionner...</option>
              {job_positions.map(job_position => (
                <option key={job_position.id} value={job_position.id}>{job_position.title}</option>
              ))}
            </select>
          </label>
          </div>
          <div className="form-group">
          <label>
            Manager :
            <select value={managerID} onChange={(e) => setManager(e.target.value)}>
              <option value="">Sélectionner...</option>
              {managers.map(manager => (
                <option key={manager.id} value={manager.id}>{manager.username}</option>
              ))}
            </select>
          </label>
          </div>
          <div className="form-group">
          <label>
            Coach :
            <select value={coachID} onChange={(e) => setCoach(e.target.value)}>
              <option value="">Sélectionner...</option>
              {coachs.map(coach => (
                <option key={coach.id} value={coach.id}>{coach.username}</option>
              ))}
            </select>
          </label>
          </div>
          <div className="form-group">
          <label>
            Address :
            <select value={addressID} onChange={(e) => setAddress(e.target.value)}>
              <option value="">Sélectionner...</option>
              {addresss.map(address => (
                <option key={address.id} value={address.id}>{address.id}</option>
              ))}
            </select>
          </label>
          </div>
                <div className="form-group">
                    <label>Departements :</label>
                    <select value={departmentID} onChange={e => setDepartment(e)} multiple>
                        {departments.map(department => (
                            <option key={department.id} value={department.id}>{department.name}</option>
                        ))}
                    </select>
                </div>
          <div className="form-group">
          <label>
            work Address :
            <select value={work_addressID} onChange={(e) => setWorkAddress(e.target.value)}>
              <option value="">Sélectionner...</option>
              {work_addresss.map(work_address => (
                <option key={work_address.id} value={work_address.id}>{work_address.id}</option>
              ))}
            </select>
          </label>
          </div>
          <label>
            Employe concernée :
            <select value={employe_concerneID} onChange={(e) => setEmploye(e.target.value)}>
              <option value="">Sélectionner...</option>
              {employe_concernes.map(employe_concerne => (
                <option key={employe_concerne.id} value={employe_concerne.id}>{employe_concerne.username}</option>
              ))}
            </select>
          </label>
          <button className="btn btn-success mt-3" type="submit">Ajouter Fiche</button>
                    <Link to="/Dashboardfiche">
                        <button className="btn btn-gray mt-3">Retour au tableau de bord</button>
                    </Link>
        </form>
      </div>
    </div>
  );
}

export default FicheForm;
