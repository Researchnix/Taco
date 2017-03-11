import React, {Component} from 'react'
import ReactDOM from 'react-dom'
import TapPlugin from 'react-tap-event-plugin'
TapPlugin();
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import getMuiTheme from 'material-ui/styles/getMuiTheme'
import App from './components/App'
import {Provider} from 'mobx-react'
import {Store} from './stores'
import './app.global.css'


const store = new Store();
ReactDOM.render(
	<Provider store={store}>
		<MuiThemeProvider muiTheme={getMuiTheme()}>
			<App/>
		</MuiThemeProvider>
	</Provider>,
	document.getElementById('root')
);