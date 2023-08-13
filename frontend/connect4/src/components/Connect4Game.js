import React, { Component } from "react";
import { w3cwebsocket as W3CWebSocket } from "websocket";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Row from "./Row";

import { WEBSOCKET_URL } from "../constants";

class Connect4game extends Component {
  constructor(props) {
    super(props);

    this.state = {
      game_id: null,
      player1: "o",
      player2: "x",
      currentPlayer: "o",
      board: [],
      gameOver: false,
      message: "",
    };
  }

  componentDidMount() {
    this.client.onopen = () => {
      console.log("WebSocket Client Connected");
    };
    this.client.onmessage = (message) => {
      const dataFromServer = JSON.parse(message.data);
      // check if message is dict or error string
      if (dataFromServer.message.constructor == Object) {
        this.setState({
          game_id: dataFromServer.message["id"],
          currentPlayer: dataFromServer.message["current_player"],
          board: dataFromServer.message["board"],
          gameOver: dataFromServer.message["game_end"],
          message: dataFromServer.message["message"],
        });
      } else {
        toast.error(dataFromServer.message);
      }
    };
  }

  getBoard = () => {
    let data = { type: "create", current_player: "o" };
    this.client.send(
      JSON.stringify({
        type: "message",
        text: data,
        sender: this.state.player1,
      })
    );
  };

  makeMove = (row, side) => {
    let data = {
      type: "update",
      line: row,
      side: side,
      player: this.state.currentPlayer,
    };
    this.client.send(
      JSON.stringify({
        type: "message",
        text: data,
        sender: this.state.currentPlayer,
      })
    );
  };
  client = new W3CWebSocket(WEBSOCKET_URL);

  render() {
    return (
      <div>
        <div
          className="button"
          onClick={() => {
            this.getBoard();
          }}
        >
          New Game
        </div>
        <div> Player 1: {this.state.player1}</div>
        <div> Player 2: {this.state.player2}</div>
        <div> Current Player: {this.state.currentPlayer}</div>
        <table>
          <thead></thead>
          <tbody>
            {this.state.board.map((row, i) => (
              <Row
                key={i}
                row={row}
                makeMove={this.makeMove}
                rowIndex={this.state.board.indexOf(row)}
              />
            ))}
          </tbody>
        </table>
        <p className="message">{this.state.message}</p>
        <ToastContainer />
      </div>
    );
  }
}

export default Connect4game;
