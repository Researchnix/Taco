import React from 'react'
import {inject, observer} from 'mobx-react'
import Paper from 'material-ui/Paper'
import {Stage, Layer, Rect} from 'react-konva'
import styled from 'styled-components'
import Street from './Street'
import Intersection from './Intersection'
import FlatButton from 'material-ui/FlatButton'


const Container = styled.div`
	width: calc(100vw - 16px);
	height: calc(100vh - 16px);
	padding: 8px;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
`;

const sizes = {
	width: 706 - 16,
	height: 706 - 16
};

@inject('store')
@observer
class App extends React.Component {
	handleClick = () => {
		this.props.store.requestUpdate();
	};

	renderStreets = () => {
		const streets = [];
		this.props.store.streets.forEach(street => {
			streets.push(<Street street={street} key={`str_${street.id}`}/>)
		});

		return streets
	};

	renderIntersections = () => {
		const intersections = [];
		this.props.store.intersections.forEach(intersection => {
			intersections.push(<Intersection intersection={intersection} key={`int_${intersection.id}`}/>)
		});

		return intersections
	};

	render() {
		return (
			<Container>
				<Paper style={sizes}>
					<Stage {...sizes}>
						<Layer>
							{this.renderStreets()}
							{this.renderIntersections()}
						</Layer>
					</Stage>
				</Paper>
				<FlatButton label="Update" primary={true} onTouchTap={this.handleClick}/>
			</Container>
		)
	}
}

export default App