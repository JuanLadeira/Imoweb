import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: 'home',
        loadChildren: () => import('./home/home.routes').then((m) => m.HomeRoutes)
    },
    // Outras rotas...
];
