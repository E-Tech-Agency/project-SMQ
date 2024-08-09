import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { FaEdit, FaList, FaTh } from 'react-icons/fa';
import '../list.css'; 

const sampleResponsables = [
    { id: 1, nom: 'Dupont', prenom: 'Jean', username: 'jdupont', email: 'jean.dupont@example.com' },
    { id: 2, nom: 'Martin', prenom: 'Marie', username: 'mmartin', email: 'marie.martin@example.com' },
    { id: 3, nom: 'Durand', prenom: 'Paul', username: 'pdurand', email: 'paul.durand@example.com' }
];

const DashboardResponsable = () => {
    const [responsables, setResponsables] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [sortConfig, setSortConfig] = useState({ key: 'id', direction: 'ascending' });
    const [viewMode, setViewMode] = useState('list');

    useEffect(() => {
        setResponsables(sampleResponsables);
    }, []);

    const sortedResponsables = React.useMemo(() => {
        let sortableResponsables = [...responsables];
        if (sortConfig !== null) {
            sortableResponsables.sort((a, b) => {
                if (a[sortConfig.key] < b[sortConfig.key]) {
                    return sortConfig.direction === 'ascending' ? -1 : 1;
                }
                if (a[sortConfig.key] > b[sortConfig.key]) {
                    return sortConfig.direction === 'ascending' ? 1 : -1;
                }
                return 0;
            });
        }
        return sortableResponsables;
    }, [responsables, sortConfig]);

    const filteredResponsables = sortedResponsables.filter(responsable =>
        responsable.nom.toLowerCase().includes(searchQuery.toLowerCase()) ||
        responsable.prenom.toLowerCase().includes(searchQuery.toLowerCase()) ||
        responsable.username.toLowerCase().includes(searchQuery.toLowerCase()) ||
        responsable.email.toLowerCase().includes(searchQuery.toLowerCase())
    );


    const requestSort = (key) => {
        let direction = 'ascending';
        if (sortConfig.key === key && sortConfig.direction === 'ascending') {
            direction = 'descending';
        }
        setSortConfig({ key, direction });
    };

    const getSortArrow = (key) => {
        if (sortConfig.key === key) {
            return sortConfig.direction === 'ascending' ? '🔼' : '🔽';
        }
        return '↕️';
    };

    return (
        <main style={{ backgroundColor: '#eeeeee', minHeight: '100vh', display: 'flex', justifyContent: 'center' }}>
            <div className="container dashboard">
                <div className="row">
                    <div>
                        <br />
                        <br />
                        <div className="table-container">
                            <div className="view-toggle">
                                <button className={`view-btn ${viewMode === 'list' ? 'active' : ''}`} onClick={() => setViewMode('list')}>
                                    <FaList /> 
                                </button>
                                <button className={`view-btn ${viewMode === 'grid' ? 'active' : ''}`} onClick={() => setViewMode('grid')}>
                                    <FaTh /> 
                                </button>
                            </div>
                            <h3 className="formation-title">Liste des Responsables</h3>
                            <div className="button-container">
                                <Link to="/DashboardRH/">
                                    <button className="retour">Retour</button>
                                </Link>
                                <Link to="/ajouter-responsable/">
                                    <button className="button-add">Ajouter Responsable</button>
                                </Link>
                            </div>
                            <br />
                            <div className="search-container">
                                <input
                                    type="text"
                                    placeholder="Rechercher..."
                                    value={searchQuery}
                                    onChange={(e) => setSearchQuery(e.target.value)}
                                    className="search-input"
                                />
                            </div>
                            <br />
                            <div>
                                {viewMode === 'list' ? (
                                    <table>
                                        <thead className="table-header">
                                            <tr>
                                                <th scope="col" onClick={() => requestSort('nom')}>
                                                    Nom Responsable {getSortArrow('nom')}
                                                </th>
                                                <th scope="col" onClick={() => requestSort('prenom')}>
                                                    Prénom Responsable {getSortArrow('prenom')}
                                                </th>
                                                <th scope="col" onClick={() => requestSort('username')}>
                                                    Nom d'utilisateur {getSortArrow('username')}
                                                </th>
                                                <th scope="col" onClick={() => requestSort('email')}>
                                                    Email Responsable {getSortArrow('email')}
                                                </th>
                                                <th scope="col">Détails</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {filteredResponsables.length > 0 ? (
                                                filteredResponsables.map(responsable => (
                                                    <tr>
                                                        <td>{responsable.nom}</td>
                                                        <td>{responsable.prenom}</td>
                                                        <td>{responsable.username}</td>
                                                        <td>{responsable.email}</td>
                                                        <td>
                                                            <Link to={`/responsable/${responsable.id}`} className="btn btn-outline-info btn-sm">
                                                                <FaEdit />
                                                            </Link>
                                                        </td>
                                                    </tr>
                                                ))
                                            ) : (
                                                <tr>
                                                    <td colSpan="6" className="text-center">Aucun responsable disponible</td>
                                                </tr>
                                            )}
                                        </tbody>
                                    </table>
                                ) : (
                                    <div className="grid">
                                        {filteredResponsables.length > 0 ? (
                                            filteredResponsables.map(responsable => (
                                                <div key={responsable.id} className="responsable-item">
                                                    <img src="https://via.placeholder.com/100" alt={`${responsable.nom} ${responsable.prenom}`} className="responsable-img" />
                                                    <div className="responsable-info">
                                                        <h5 className="responsable-title">{responsable.nom} {responsable.prenom}</h5>
                                                        <p><strong className="responsable-text">Nom d'utilisateur :</strong> {responsable.username}</p>
                                                        <p><strong className="responsable-text">Email :</strong> {responsable.email}</p>
                                                        <Link to={`/responsable/${responsable.id}`} className="btn btn-outline-info btn-sm">
                                                            <FaEdit />
                                                        </Link>
                                                    </div>
                                                </div>
                                            ))
                                        ) : (
                                            <p className="text-center">Aucun responsable disponible</p>
                                        )}
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    );
};

export default DashboardResponsable;
