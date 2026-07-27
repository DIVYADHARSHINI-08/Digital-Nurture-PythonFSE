import { ErrorHandler, Injectable } from '@angular/core';

@Injectable()
export class GlobalErrorHandlerService implements ErrorHandler {

  handleError(error: any): void {

    // Log the error
    console.error('Global Error:', error);

    // Show fallback message
    alert('Something went wrong! Please try again later.');

  }

}