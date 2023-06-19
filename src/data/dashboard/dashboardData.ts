import type { recents, activeProjectsData } from '@/types/dashboard/index';

const activeProjectsData = [];

const statusColors = {
    'Esperando Scorecard': '#003f5c',
    'Análisis': '#7a5195',
    'Esperando Aprobación': '#ef5675',
    'Esperando Inversión': '#ffa600',
    'Activo': '#bc5090',
    'En Evaluación': '#ffa600',
    'Finalizando': '#58508d'
};

const recentEvals: recents[] = [
    {
        date: '01/01/2023',
        description: 'Evaluación nueva para el proyecto EducTech',
        textcolor: '#003f5c',
        boldtext: false,
        line: true,
        link: 'EducTech',
        url: ''
    },
    {
        date: '15/03/2023',
        description: 'Evaluación nueva para la campaña VacunaYa',
        textcolor: '#003f5c',
        boldtext: false,
        line: true,
        link: 'VacunaYa',
        url: ''
    },
    {
        date: '10/05/2023',
        description: 'Evaluación nueva para el proyecto BosqueVivo',
        textcolor: '#003f5c',
        boldtext: false,
        line: true,
        link: 'BosqueVivo',
        url: ''
    },
    {
        date: '20/07/2023',
        description: 'Scorecard nueva para el programa Impulso PYME',
        textcolor: '#003f5c',
        boldtext: true,
        line: true,
        link: 'Impulso PYME',
        url: ''
    },
    {
        date: '05/09/2023',
        description: 'Evaluación nueva para la campaña IgualdadAhora',
        textcolor: '#003f5c',
        boldtext: false,
        line: true,
        link: 'IgualdadAhora',
        url: ''
    },
    {
        date: '12/11/2023',
        description: 'Scorecard nueva para el programa SeguroVecino',
        textcolor: '#003f5c',
        boldtext: true,
        line: true,
        link: 'SeguroVecino',
        url: ''
    }
]

/*Basic Table 1*/
const activeProjects: activeProjectsData[] = [
    {
        "id": 1,
        "name": "María González",
        "category": "Reforma educativa",
        "subcategory": "Inversión en tecnología",
        "pname": "EducTech",
        "status": "Esperando Inversión",
        "statuscolor": "#FF4500",
        "budget": "$10,000"
    },
    {
        "id": 2,
        "name": "Carlos Ramírez",
        "category": "Salud pública",
        "subcategory": "Campaña de vacunación",
        "pname": "VacunaYa",
        "status": "Activo",
        "statuscolor": "#00FF00",
        "budget": "$8,500"
    },
    {
        "id": 3,
        "name": "Luisa Fernández",
        "category": "Medio ambiente",
        "subcategory": "Proyecto de reforestación",
        "pname": "BosqueVivo",
        "status": "Esperando Aprobación",
        "statuscolor": "#FFD700",
        "budget": "$12,700"
    },
    {
        "id": 4,
        "name": "Antonio Méndez",
        "category": "Economía",
        "subcategory": "Programa de apoyo a PYMEs",
        "pname": "Impulso PYME",
        "status": "En Evaluación",
        "statuscolor": "#8A2BE2",
        "budget": "$15,000"
    },
    {
        "id": 5,
        "name": "Ana Pérez",
        "category": "Derechos humanos",
        "subcategory": "Campaña contra la discriminación",
        "pname": "IgualdadAhora",
        "status": "Finalizando",
        "statuscolor": "#A9A9A9",
        "budget": "$7,600"
    },
    {
        "id": 6,
        "name": "Jorge Sánchez",
        "category": "Seguridad ciudadana",
        "subcategory": "Programa de vigilancia comunitaria",
        "pname": "SeguroVecino",
        "status": "Esperando Scorecard",
        "statuscolor": "#00BFFF",
        "budget": "$9,800"
    }
];

export { recentEvals, activeProjects }
