import webpack from 'webpack'
import path from 'path';
import autoprefixer from 'autoprefixer'
import ExtractTextPlugin from 'extract-text-webpack-plugin'

export default {
	module:    {
		noParse: [
			/node_modules[\/\\]json-schema[\/\\]lib[\/\\]validate\.js/
		],
		rules: [{
			test:    /\.jsx?$/,
			use: [
				{
					loader: 'babel-loader',
					options: {
						babelrc: false,
						extends: path.join(__dirname, '..', '.babelrc-webpack')
					}
				}
			],
			exclude: /node_modules/
		}, {
			test: /\.(eot|ttf|woff|woff2)$/,
			use: [
				{
					loader: 'file-loader',
					options: {
						name: 'public/fonts/[name].[ext]'
					}
				}
			]
		}]
	},
	output:    {
		path:          path.join(__dirname, '..', 'dist'),
		filename:      'bundle.js',
		libraryTarget: 'commonjs2'
	},
	resolve:   {
		extensions: ['.js', '.jsx', '.json'],
		mainFields: ['browser', 'web', 'main'],
		// mainFields: ['webpack', 'browser', 'web', 'browserify', ['jam', 'main'], 'main'],
		alias: {
			'app': path.join(__dirname, '..', 'app')
		}
	},
	plugins:   [
		new webpack.IgnorePlugin(/^(canvas|jsdom)$/) // for konva
	],
	externals: [
		// put your node 3rd party libraries which can't be built with webpack here
		// (mysql, mongodb, and so on..)
	]
};