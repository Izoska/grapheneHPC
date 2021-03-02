package com.LJ.StockSafe.model.service;

import java.util.List;

import com.LJ.StockSafe.model.dto.StockDto;

public interface StockService {

	boolean createStock(StockDto stockdto);
	List<StockDto> readStockAll(String keyword);
	List<StockDto> readStockAllbyTag(String tag, String keyword);
	StockDto readStockDetail(String id);
	boolean updateStock(StockDto stockdto);
	boolean deleteStock(String id);
}
