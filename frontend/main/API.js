import {ipcMain} from 'electron'
import {IPC_PYTHON, IPC_INITIAL_REQ, IPC_INITIAL_RES, IPC_UPDATE_REQ, IPC_UPDATE_RES} from '../constants'
import PythonShell from 'python-shell'
import stub from './stub.json'


export class API {
	webContents;

	constructor(webContents) {
		this.webContents = webContents;
		ipcMain.on(IPC_INITIAL_REQ, this.getInitial);
		ipcMain.on(IPC_UPDATE_REQ, this.getUpdates);
	}

	getInitial = () => {
		this.sendInitial(stub);
	};

	getUpdates = () => {
		// const obj = JSON.parse(stub);
		const obj = stub;
		obj.streets.forEach(street => {
			street.percent = Math.random();
		});
		obj.intersections = [];
		console.log({obj});
		this.sendUpdates(obj);
	};

	sendInitial = (json) => {
		this.webContents.send(IPC_INITIAL_RES, json);
	};

	sendUpdates = (json) => {
		this.webContents.send(IPC_UPDATE_RES, json);
	}
}