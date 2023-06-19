import {
    DashboardIcon,
    CalendarIcon,
    BriefcaseIcon,
    CurrencyDollarIcon,
    MapPinIcon,
    MessageCircleIcon,
    PhoneIcon,
    UserCheckIcon,
    StarIcon,
    UsersIcon,
    UserPlusIcon,
    MapIcon,
    TrendingUpIcon,
    ChartBarIcon,
    FileTextIcon,
    FileIcon,
    AwardIcon,
    SocialIcon,
    GavelIcon
} from 'vue-tabler-icons';

export interface menu {
    header?: string;
    title?: string;
    icon?: any;
    to?: string;
    chip?: string;
    chipColor?: string;
    chipVariant?: string;
    chipIcon?: string;
    children?: menu[];
    disabled?: boolean;
    type?: string;
    subCaption?: string;
}

const sidebarItem: menu[] = [
    { header: 'Inicio' },
    {
        title: 'Dashboard',
        icon: DashboardIcon,
        to: '/'
    },
    { header: 'Administración' },
    {
        title: 'Calendario',
        icon: CalendarIcon,
        to: '/ui/calendario'
    },
    {
        title: 'Gestión de Labores',
        icon: BriefcaseIcon,
        to: '/ui/gestion-de-labores'
    },
    {
        title: 'Finanzas',
        icon: CurrencyDollarIcon,
        to: '/ui/finanzas'
    },
    {
        title: 'Geovisualizador',
        icon: MapPinIcon,
        to: '/ui/geovisualizador'
    },
    {
        title: 'Radar Legal',
        icon: GavelIcon,
        to: '/ui/radar-legal'
    },
    { header: 'Comunicación Masiva' },
    {
        title: 'Redes Sociales',
        icon: SocialIcon,
        to: '/ui/redes-sociales'
    },
    {
        title: 'Whatsapp',
        icon: MessageCircleIcon,
        to: '/ui/whatsapp'
    },
    {
        title: 'Teléfonos',
        icon: PhoneIcon,
        to: '/ui/telefonos'
    },
    { header: 'Maquinaria Política' },
    {
        title: 'Voluntarios',
        icon: UserCheckIcon,
        to: '/ui/voluntarios'
    },
    {
        title: 'Promovidos',
        icon: StarIcon,
        to: '/ui/promovidos'
    },
    {
        title: 'Coordinadores',
        icon: UsersIcon,
        to: '/ui/coordinadores'
    },
    {
        title: 'RGs y RCS',
        icon: UserPlusIcon,
        to: '/ui/rgs-y-rcs'
    },
    {
        title: 'VIPs',
        icon: StarIcon,
        to: '/ui/vips'
    },
    { header: 'InteliStats' },
    {
        title: 'Mapas',
        icon: MapIcon,
        to: '/ui/mapas'
    },
    {
        title: 'Social Listening',
        icon: TrendingUpIcon,
        to: '/ui/social-listening'
    },
    {
        title: 'Mediciones',
        icon: ChartBarIcon,
        to: '/ui/mediciones'
    },
    {
        title: 'Informes',
        icon: FileTextIcon,
        to: '/ui/informes'
    },
    { header: 'Varios' },
    {
        title: 'Dossier',
        icon: FileIcon,
        to: '/ui/dossier'
    },
    {
        title: 'Plataforma Política',
        icon: AwardIcon,
        to: '/ui/plataforma-politica'
    },
];

export default sidebarItem;
