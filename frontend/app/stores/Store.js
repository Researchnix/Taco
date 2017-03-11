import {observable, action, autorun, toJS} from 'mobx'
import {Street} from './Street'
import {Intersection} from './Intersection'
import {ipcRenderer} from 'electron'
import {IPC_INITIAL_RES, IPC_INITIAL_REQ, IPC_UPDATE_REQ, IPC_UPDATE_RES} from '../../constants'


export class Store {
	@observable streets = new Map();
	@observable intersections = new Map();

	@action.bound handleInitial(event, json) {
		json.streets.forEach(street => {
			this.streets.set(street.id, new Street(street))
		});

		json.intersections.forEach(intersection => {
			this.intersections.set(intersection.id, new Intersection(intersection))
		})
	}

	@action.bound handleUpdate(event, json) {
		json.streets.forEach(street => {
			this.streets.get(street.id).update(street);
		});

		json.intersections.forEach(intersection => {
			this.intersections.get(intersection.id).update(intersection);
		});
	}

	requestUpdate = () => {
		ipcRenderer.send(IPC_UPDATE_REQ);
	};

	constructor() {
		ipcRenderer.on(IPC_INITIAL_RES, this.handleInitial);
		ipcRenderer.on(IPC_UPDATE_RES, this.handleUpdate);
		ipcRenderer.send(IPC_INITIAL_REQ);
	}
}