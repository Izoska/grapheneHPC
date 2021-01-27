
package com.LJ.StockSafe.controller;

import java.io.IOException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.LJ.StockSafe.model.dto.PriceDto;
import com.LJ.StockSafe.model.dto.StockDto;
import com.LJ.StockSafe.model.service.StockService;
import com.LJ.StockSafe.util.FinanceUtil;

@RestController
@RequestMapping("/stock")
@CrossOrigin(origins = "*")
public class StockController {

	@Autowired
	StockService stockService;
	
	@Autowired
	FinanceUtil financeUtil;
	
	private static final String SUCCESS = "success";
	private static final String FAIL = "fail";
	
	@PostMapping
	public ResponseEntity<String> createStock(@RequestBody StockDto stockdto){
		if(stockService.createStock(stockdto)) return new ResponseEntity<String>(SUCCESS, HttpStatus.OK);
		return new ResponseEntity<String>(FAIL, HttpStatus.NO_CONTENT);
	}
	
	@GetMapping
	public ResponseEntity<StockDto> readStockDetail(String id){
		return new ResponseEntity<StockDto>(stockService.readStockDetail(id), HttpStatus.OK);  
	}
	
	@GetMapping("/price")
	public ResponseEntity<PriceDto> readPrice(String id) throws IOException{
		return new ResponseEntity<PriceDto>(financeUtil.readPrice(id), HttpStatus.OK);  
	}
	
	@GetMapping("/searchAll")
	public ResponseEntity<List<StockDto>> readStockAll(String keyword){
		return new ResponseEntity<List<StockDto>>(stockService.readStockAll(keyword), HttpStatus.OK);  
	}

	@GetMapping("/searchAllbyTag")
	public ResponseEntity<List<StockDto>> readStockAllbyTag(@RequestParam(value="tag") String tag, @RequestParam(value="keyword") String keyword){
		return new ResponseEntity<List<StockDto>>(stockService.readStockAllbyTag(tag, keyword), HttpStatus.OK);
	}

	@PutMapping
	public ResponseEntity<String> updateStock(@RequestBody StockDto stockdto){
		if(stockService.updateStock(stockdto)) return new ResponseEntity<String>(SUCCESS, HttpStatus.OK);
		return new ResponseEntity<String>(FAIL, HttpStatus.NO_CONTENT);
	}
	
	@DeleteMapping
	public ResponseEntity<String> deleteStock(String id){
		if(stockService.deleteStock(id)) return new ResponseEntity<String>(SUCCESS, HttpStatus.OK);
		return new ResponseEntity<String>(FAIL, HttpStatus.NO_CONTENT);
	}
	
}