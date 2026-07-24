import { createReducer, on } from '@ngrx/store';
import * as CourseActions from './courses.actions';

export interface CourseState {
  loading: boolean;
}

export const initialState: CourseState = {
  loading: false
};

export const coursesReducer = createReducer(
  initialState,

  on(CourseActions.loadCourses, (state) => ({
    ...state,
    loading: true
  }))
);