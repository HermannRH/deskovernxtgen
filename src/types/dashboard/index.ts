/*Recent Transaction*/
type recents = {
    date: string;
    description: string;
    textcolor: string;
    boldtext: boolean;
    line: boolean;
    link: string;
    url: string;
};

/*product performance*/
type activeProjectsData = {
    id: number;
    name: string;
    category: string;
    subcategory: string;
    pname: string;
    status: string;
    statuscolor: string;
    budget: string;
};

export type { recents, activeProjectsData }