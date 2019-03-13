import * as actionTypes from '../actions/actionTypes';

const initialState = {
    username: '',
    error: null,
    loading: false,
};

const reducer = ( state = initialState, action ) => {
    if (action.type === actionTypes.AUTH_START) {
        return {
            ...initialState,
            loading: true,
        };
    }

    if (action.type === actionTypes.AUTH_SUCCESS) {
        return {
            ...initialState,
            username: action.username,
        }
    }

    if (action.type === actionTypes.AUTH_FAILED) {
        return {
            ...initialState,
            error: action.error
        }
    }

    if (action.type === action.USER_LOGOUT) {
        return {
            ...initialState,
        }
    }

    return state;
};

export default reducer;