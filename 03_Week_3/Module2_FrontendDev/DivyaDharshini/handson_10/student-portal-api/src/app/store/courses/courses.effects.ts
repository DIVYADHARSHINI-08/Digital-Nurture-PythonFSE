import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { tap } from 'rxjs/operators';
import * as CourseActions from './courses.actions';

@Injectable()
export class CoursesEffect {

  loadCourses$ = createEffect(
    () =>
      this.actions$.pipe(
        ofType(CourseActions.loadCourses),
        tap(() => {
          console.log('Calling CourseService...');
        })
      ),
    { dispatch: false }
  );

  constructor(private actions$: Actions) {}
}

/*
Data Flow:

Component
    |
dispatch(loadCourses())
    |
Action
    |
Effect
    |
CourseService (API)
    |
Reducer
    |
Store State
    |
Selector
    |
Component
*/