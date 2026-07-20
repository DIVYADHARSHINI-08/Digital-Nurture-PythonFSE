import { ApplicationConfig, provideBrowserGlobalErrorListeners } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideStore } from '@ngrx/store';
import { provideEffects } from '@ngrx/effects';

import { ErrorHandler } from '@angular/core';
import { GlobalErrorHandlerService } from './services/global-error-handler.service';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideRouter(routes),
    provideStore(),
    provideEffects(),
    {
      provide: ErrorHandler,
      useClass: GlobalErrorHandlerService
    }
  ],
};
