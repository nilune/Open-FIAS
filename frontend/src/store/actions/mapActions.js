import * as actionTypes from './actionTypes';
import axios from "axios";
import { notesServer, geocoderServer } from "../serverURLs";

const saveData = (actionType, latitude, longitude, address, zoom) => {
    return {
        type: actionType,
        address,
        lat: latitude,
        lng: longitude,
        zoom
    }
};

const start = (actionType) => {
    return {
        type: actionType
    }
};

const failed = (actionType, error) => {
    return {
        type: actionType,
        error
    }
};

const getStart = (address) => {
    return {
        type: actionTypes.GET_COORDS_START,
        address
    }
};

export const getCoords = (address) => {
    return function (dispatch) {
        dispatch(getStart(address));
        return axios.get(geocoderServer, {
                params: {
                    address
                }
            }).then( resp => {
                if (resp.data.features && resp.data.features[0].geometry) {
                    const coords = resp.data.features[0].geometry.coordinates;
                    let zoom = resp.data.features[0].rank || resp.data.features[0].properties.rank;
                    console.log(zoom);
                    dispatch(saveData(actionTypes.GET_COORDS_SUCCESS, coords[0], coords[1], address, zoom))
                } else {
                    dispatch(failed(actionTypes.GET_COORDS_FAILED, 'места не найдены'))
                }
            }).catch(error => {
                dispatch(failed(actionTypes.GET_COORDS_FAILED, error))
            });
    }
};

export const sendLink = (address, coords) => {
    return function (dispatch) {
        dispatch(start(actionTypes.SENDING_LINK_START));
        return axios.post(notesServer, {
            address,
            lat: coords.lat,
            lon: coords.lng
        }, { withCredentials: true }).then( resp => {
            dispatch(start(actionTypes.SENDING_LINK_SUCCESS));
            localStorage.setItem('hasAddedPoints', 'true');
        }).catch(error => {
            if (error.response && error.response.status === 400) {
                if (error.response.data === 'You done too many points') {
                    dispatch(failed(actionTypes.SENDING_LINK_FAILED, { message: 'превышен лимит точек' }))
                } else {
                    dispatch(failed(actionTypes.SENDING_LINK_FAILED, { message: 'некорректный адрес' }))
                }
            } else {
                dispatch(failed(actionTypes.SENDING_LINK_FAILED, error))
            }
        });
    }
};



export const setAddress = (address) => {
    return {
        type: actionTypes.SET_ADDRESS,
        address
    }
};

export const setMapCoords = (coords) => {
    return {
        type: actionTypes.SET_MAP_COORDS,
        lat: coords.lat,
        lng: coords.lng
    }
};

export const unfocusInput = () => {
    return {
        type: actionTypes.UNFOCUS_INPUT
    }
};

export const clearData = () => {
    return {
        type: actionTypes.CLEAR_DATA
    }
};