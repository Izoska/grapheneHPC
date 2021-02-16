
package com.LJ.StockSafe.model.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.LJ.StockSafe.model.dto.StockDto;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface StockMapper {
	int createStock(StockDto stockdto);
	List<StockDto> readStockAll(String keyword);
	List<StockDto> readStockAllbyTag(@Param("tag") String tag, @Param("keyword")String keyword);
	StockDto readStockDetail(String id);
	int updateStock(StockDto stockdto);
	int deleteStock(String id);
}