import React from 'react'
import {Stage, Layer, Rect} from 'react-konva'


class App extends React.Component {
	render() {
		return (
			<Stage width={1024} height={768}>
				<Layer>
					<Rect x={10} y={10} width={5} height={5} fill='green'/>
				</Layer>
			</Stage>
		)
	}
}

export default App