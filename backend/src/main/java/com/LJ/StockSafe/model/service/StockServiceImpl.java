
package com.LJ.StockSafe.model.service;

import java.util.List;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.LJ.StockSafe.model.dto.StockDto;
import com.LJ.StockSafe.model.mapper.StockMapper;

@Service
public class StockServiceImpl implements StockService{

	private Logger logger = LogManager.getLogger(this.getClass());

	@Autowired
	StockMapper stockmapper;
	
	@Override
	public boolean createStock(StockDto stockdto) {
		// TODO Auto-generated method stub
		if(stockmapper.createStock(stockdto) == 1) return true;
		return false;
	}

	@Override
	public List<StockDto> readStockAll(String keyword) {
		// TODO Auto-generated method stub
		
		List<StockDto> stockDtoList = stockmapper.readStockAll(keyword);
		
		//결과 출력을 log4j를 이용해 출력.
		logger.info(stockDtoList);
		//for(int a=0; a<temp.size(); a++) System.out.println(temp.toString());
				
		return stockDtoList;
	}

	@Override
	public List<StockDto> readStockAllbyTag(String tag, String keyword) {
		// TODO Auto-generated method stub

		System.out.println(tag + ", " + keyword);
		List<StockDto> temp = stockmapper.readStockAllbyTag(tag, keyword);

		for(int a=0; a<temp.size(); a++) System.out.println(temp.toString());

		return temp;
	}

	@Override
	public StockDto readStockDetail(String id) {
		// TODO Auto-generated method stub
		return stockmapper.readStockDetail(id);
	}

	@Override
	public boolean updateStock(StockDto stockdto) {
		// TODO Auto-generated method stub
		if(stockmapper.updateStock(stockdto)==1) return true;
		return false;
	}

	@Override
	public boolean deleteStock(String id) {
		// TODO Auto-generated method stub
		if(stockmapper.deleteStock(id)==1) return true;
		return false;
	}

}