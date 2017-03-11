import {app, BrowserWindow, ipcMain} from 'electron'
import Promise from 'bluebird'
import configureTemplate from './configureTemplate'
import {API} from './API'
// import getToken from './getToken'
// import getId from './getId'
// import {TinderApi} from './tinderApi'
// import showNotification from './showNotification'
// import {FB_GET_TOKEN_REQUEST, FB_GET_ID_REQUEST, TINDER_API, SHOW_NOTIFICATION} from '../app/constants'

let mainWindow = null;


// if (process.env.NODE_ENV === 'development') {
// 	require('electron-debug')(); // eslint-disable-line global-require
// }

// For production tests!!
require('electron-debug')();


app.on('window-all-closed', () => {
	if (process.platform !== 'darwin') app.quit();
});


const installExtensions = async () => {
	if (process.env.NODE_ENV === 'development') {
		const installer = require('electron-devtools-installer'); // eslint-disable-line global-require

		const extensions = [
			'REACT_DEVELOPER_TOOLS'
		];
		const forceDownload = !!process.env.UPGRADE_EXTENSIONS;
		if (forceDownload) {
			for (const name of extensions) {
				console.log(name);
				try {
					await installer.default(installer[name], forceDownload);
				} catch (e) {} // eslint-disable-line
			}
		}
	}
};

function reload(win) {
	if (process.env.NODE_ENV === 'development') {
		win.loadURL(`file://${__dirname}/../app/index.html`);
	} else {
		win.loadURL(`file://${__dirname}/app/index.html`);
	}
}

app.on('ready', async () => {
	await installExtensions();

	mainWindow = new BrowserWindow({
		show:   false,
		width:  1024,
		height: 728,
		minWidth: 1024,
		minHeight: 728,
		maxWidth: 1024,
		maxHeight: 728,
		webPreferences: {
			blinkFeatures: 'CSSStickyPosition'
		}
	});

	// const tinderApi = new TinderApi(() => logout(mainWindow));
	// ipcMain.on(FB_GET_TOKEN_REQUEST, getToken);
	// ipcMain.on(FB_GET_ID_REQUEST, getId);
	// ipcMain.on(TINDER_API, tinderApi.handleRequest);
	// ipcMain.on(SHOW_NOTIFICATION, showNotification)
	//
	const api = new API(mainWindow.webContents);
	reload(mainWindow);

	mainWindow.webContents.on('did-finish-load', () => {
		mainWindow.show();
		mainWindow.focus();
	});

	mainWindow.on('closed', () => {
		mainWindow = null;
	});

	configureTemplate(mainWindow);
});
